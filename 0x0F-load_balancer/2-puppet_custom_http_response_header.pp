# Creates a custom HTTP header response using Puppet

exec { 'update':
  command => 'sudo apt-get update',
  provider => shell,
}
-> package { 'nginx':
  ensure => installed,
}
-> file_line { 'http_header':
  path => '/etc/nginx/nginx.conf',
  line => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'http {',
}
-> exec {'restart service':
  command => 'service nginx restart',
  provider => shell,
}
