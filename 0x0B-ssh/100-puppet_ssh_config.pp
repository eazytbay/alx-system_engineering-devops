#This uses puppet to make changes to the default ssh config file
# so that one can connect to a server without typing a password.
file_line { 'Turning off passwordauthentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line { 'IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
