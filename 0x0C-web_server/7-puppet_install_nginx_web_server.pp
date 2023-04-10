# Installs, configures, and starts the server
class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!\n',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    if (\$request_filename ~ redirect_me) {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }
}",
    require => Package['nginx'],
    notify => Service['nginx'],
  }

  exec { 'ufw_allow_nginx':
    command => '/usr/sbin/ufw allow "Nginx HTTP"',
    unless => '/usr/sbin/ufw status | grep "Nginx HTTP" | grep "ALLOW"',
    require => Package['nginx'],
  }
}

include nginx_server

