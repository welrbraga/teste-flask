#!/bin/bash

url="teste.lan:5000"
curl $url
echo
echo

curl -L $url/about
echo
curl $url/about/
echo
echo

curl -L $url/nome
echo
curl $url/nome/
echo
echo

curl -L $url/nome/welington
echo
curl $url/nome/welington/
echo
