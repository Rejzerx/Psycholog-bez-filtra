/* Psycholog bez filtra — Google Analytics 4.
   UWAGA: uruchamia pomiar bez uprzedniej zgody użytkownika.
   Przed wdrożeniem zweryfikuj zgodność z przepisami o prywatności i cookies. */
(function () {
  'use strict';
  var MEASUREMENT_ID = 'G-PMX12ZB964';
  if (window.__pbfGA4Initialized) return;
  window.__pbfGA4Initialized = true;
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', MEASUREMENT_ID);
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(MEASUREMENT_ID);
  document.head.appendChild(script);
})();
