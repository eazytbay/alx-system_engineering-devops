# This kills a process called "killmenow"
# Usage - puppet
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
