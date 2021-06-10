pipeline {
  agent any
  stages {
    stage('abc') {
      steps {
        echo 'starting now'
      }
    }

    stage('main1') {
      steps {
        sh '''#!/bin/bash


date
ls -ltr'''
      }
    }

    stage('send_emails') {
      steps {
        mail(subject: 'program updates', body: 'This is to notify that..', from: 'Pranay.gore@cg.com', to: 'Ajeet.kum@cg.com', cc: 'iffy.ma@cg.com')
      }
    }

  }
}