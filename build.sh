#!/bin/sh
set -e
set +x
cd backend && docker build -t backendforst:latest .
