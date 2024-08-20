# client config file using Puppet

file_line { 'identity file':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line {'turn off password authentication':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
  replace => true,
}
