#custom HTTP header with Puppet
class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page",
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
  }

  file { '/etc/nginx/sites-enabled/default':
    content => template('nginx_custom_header/nginx.conf.erb'),
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/nginx.conf':
    content => template('nginx_custom_header/nginx.conf.erb'),
    mode    => '0644',
    owner   => 'root',
    group   => 'root',
    notify  => Service['nginx'],
  }

  firewall { 'Nginx HTTP':
    port   => '80',
    proto  => 'tcp',
    action => 'accept',
  }
}
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  root /var/www/html;
  index index.html index.htm index.nginx-debian.html;
  server_name _;

  location / {
    try_files $uri $uri/ =404;
  }

  if ($request_filename ~ redirect_me) {
    rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
  }

  error_page 404 /404.html;

  location = /404.html {
    internal;
  }

  add_header X-Served-By <%= @hostname %>;
}

