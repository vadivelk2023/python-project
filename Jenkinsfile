pipeline {
    agent {
            label 'docker-agent-alphine'
    }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                # Build Number
echo "Build Number: ${BUILD_ID}"
echo "Build URL: ${BUILD_URL}"
pwd
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Making uv accessible everywhere
. $HOME/.local/bin/env

# Install Python version required and dependencies
uv sync

# Activating Env
. .venv/bin/activate
'''
            }
        }
        stage('Test') {
            steps {
                sh '''
                pytest
                '''
            }
        }
        stage('Run') {
            steps {
                sh '''
                python src/example.py
                '''
            }
        }
    }
}
