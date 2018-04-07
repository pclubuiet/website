var cacheName = 'pclubapp-cache';
var urlsToCache = [
  '/',
  '/home/',
  '/home/resources/',
  '/static/home/base.css',
  'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css',
  'https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css',
  'https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js',
  'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css.map',
  'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js'
];



self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request)
    .then(function (response) {
      event.waitUntil(addToCache(event.request, response.clone()));
      return response;
    })
    .catch(function(error) {
        return caches.open(cacheName).then(function(cache) {
          return cache.match(event.request);
      });
    }));
});


function addToCache(event, response) {
  caches.open(cacheName).then(function(cache) {
    cache.put(event, response);
  });
}
