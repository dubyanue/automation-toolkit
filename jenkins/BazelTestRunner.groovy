pipeline {

    agent {
        node { label params.NODE ?: 'linux' }
    }

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }

    stages {
        stage('Build') {
            steps {
                echo "Running ${BUILD_TAG} on ${env.NODE_NAME} with ${env.NODE_LABELS}..."
                echo 'Cleaning workspace...'
                cleanWs(
                    disableDeferredWipeout: true,
                    deleteDirs: true,
                )

                echo "Building ${env.JOB_NAME} in ${env.WORKSPACE}..."
                checkout scmGit(
                    branches: [[name: "${params.BRANCH}"]],
                    userRemoteConfigs: [[url: 'git@github.com:dubyanue/automation-toolkit.git']]
                )
                sh 'bazel build //...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh "bazel test --test_output=all //${params.SUITE}"
            }
        }
    }

    post {
        always {
            script {
                String suite = params.SUITE
                String[] suitesplit = suite.split(':')
                String suitename = suitesplit[1]

                echo 'Attempting to merge test results before stopping environment...'
                try {
                    sh """
                        junitparser \
                        merge \
                        --suite-name=${suitename} \
                        \$(find bazel-testlogs/ -type f -name test.xml) \
                        results.xml \
                        || echo 'Failed to merge test results'
                    """
                } catch (e) {
                    echo "Failed to merge test results: ${e.message}"
                }

                sh 'find -L ./bazel-testlogs/ -type f -name "report.html" -exec cp {} ./reports/ \\;'

                try {
                    junit 'results.xml'

                    recordCoverage(
                        tools: [[parser: 'COBERTURA', pattern: 'bazel-testlogs/**/test.outputs/coverage.xml']],
                        id: 'bazel-coverage',
                        name: 'Bazel Test Coverage'
                    )

                    publishHTML([
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'report.html',
                        reportName: 'Test Report'
                    ])

                    // publishHTML([
                    //     allowMissing: true,
                    //     alwaysLinkToLastBuild: true,
                    //     keepAll: true,
                    //     reportDir: 'reports/coverage',
                    //     reportFiles: 'index.html',
                    //     reportName: 'Coverage Report'
                    // ])

                } catch (e) {
                    echo "Failed to publish JUnit results: ${e.message}"
                }
            }
        }

        cleanup {
            sh 'bazel clean --expunge || true'
            cleanWs(disableDeferredWipeout: true, deleteDirs: true)
        }
    }

}
