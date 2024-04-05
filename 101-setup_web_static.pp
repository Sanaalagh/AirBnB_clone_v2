# 101-setup_web_static.pp
file {
  '/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu';

  '/data/web_static':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu';

  '/data/web_static/releases':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu';

  '/data/web_static/shared':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu';

  '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu';

  '/data/web_static/releases/test/index.html':
    ensure  => present,
    mode    => '0644',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n";

  '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    require => File['/data/web_static/releases/test/index.html'];
}

exec { 'nginx-service-reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('path/to/your/template.erb'),
  notify  => Exec['nginx-service-reload'],
}

