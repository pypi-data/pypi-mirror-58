# openpgp-requests
A python v3 wrapper to the inspirational "requests" module that adds some OpenPGP features.

Of course, using this requires a server-side component, which you can find
on the [python-flask-restful-openpgp-proxy](https://github.com/buanzo/python-http-openpgp-api-tools/tree/master/python-flask-restful-openpgp-proxy)
github repo.

## Introduction

This repository contains the code for the python v3 package
openpgp-requests, which is useful if you want to encrypt/sign/verify/decrypt
API requests/responses.

The code is functional, but not strongly designed with security in mind.  It
is a Proof of Concept which I expect people with more time than myself to
improve upon or be inspired by.

The server has better security for the passphrase, check it out.

## Examples

Please check [the examples folder in this repo](https://github.com/buanzo/openpgp-requests/tree/master/examples).

Cheers.
Buanzo.
