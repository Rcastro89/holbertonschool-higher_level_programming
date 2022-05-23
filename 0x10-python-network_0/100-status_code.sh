#!/bin/bash
# Take in URL, display status code only; Usage: ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
curl -s -w "%{response_code}" -o /dev/null "$1"
