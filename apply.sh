#!/bin/bash

kubectl kustomize | kubectl apply -f -
