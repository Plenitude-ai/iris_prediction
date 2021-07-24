#!/bin/bash
gunicorn --chdir src main:app -b 0.0.0.0:5000