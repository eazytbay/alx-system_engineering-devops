#!/usr/bin/env ruby
# This is a regular expression that matches a string that begins with h and
# ends with n and can have any single character in between
puts ARGV[0].scan(/h.n/).join
