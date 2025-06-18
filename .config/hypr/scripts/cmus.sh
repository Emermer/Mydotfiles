#!/bin/bash
cmus-remote -C clear
cmus-remote -C "add ~/Music/playlist/"
cmus-remote -C "update-cache -f"
