#! /bin/bash

# use git fsck (verify the validity and conenctivity)
# change to the dangling commit reported
cd my-secret-stash-repo
git checkout --quiet 14a5c7088e7638abb2232c8cac1c7dd4687819f0
cat secrets
cd ..

