/* Psycholog bez filtra — GA4. Analytics is loaded only after affirmative consent. */
(function () {
  'use strict';
  var MEASUREMENT_ID = 'G-PMX12ZB964';
  var KEY = 'pbf_analytics_consent_v1';
  var enabled = false;
  function readChoice() { try { return localStorage.getItem(KEY); } catch (_) { return null; } }
  function saveChoice(value) { try { localStorage.setItem(KEY, value); } catch (_) {} }
  function enableAnalytics() {
    if (enabled) return;
    enabled = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', MEASUREMENT_ID, { anonymize_ip: true });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(MEASUREMENT_ID);
    document.head.appendChild(s);
  }
  function hideBanner() { var el = document.getElementById('pbf-consent'); if (el) el.remove(); }
  function choose(choice) { saveChoice(choice); hideBanner(); if (choice === 'yes') enableAnalytics(); }
  function showBanner() {
    if (document.getElementById('pbf-consent')) return;
    var style = document.createElement('style');
    style.textContent = '#pbf-consent{position:fixed;z-index:2147483000;bottom:16px;left:16px;right:16px;max-width:590px;margin:0 auto;background:#fffaf5;color:#252321;border:1px solid #d8ccc0;box-shadow:0 15px 50px #0003;border-radius:17px;padding:20px;font:15px/1.55 system-ui,-apple-system,sans-serif}#pbf-consent p{margin:6px 0 15px;font-size:14px;line-height:1.55;color:#4e4944}#pbf-consent strong{font-size:16px}#pbf-consent .pbf-actions{display:flex;gap:10px;flex-wrap:wrap}#pbf-consent button{border-radius:9px;padding:11px 17px;font:600 14px system-ui;cursor:pointer;border:1px solid #b3454c}#pbf-consent .pbf-accept{background:#ad4149;color:#fff}#pbf-consent .pbf-reject{background:transparent;color:#68292e}#pbf-privacy-settings{position:fixed;z-index:2147482999;left:12px;bottom:12px;border:1px solid #d8ccc0;background:#fffaf5;color:#49413e;padding:7px 11px;border-radius:8px;font:12px system-ui;cursor:pointer;opacity:.88}';
    document.head.appendChild(style);
    var el = document.createElement('section'); el.id = 'pbf-consent'; el.setAttribute('role','dialog'); el.setAttribute('aria-label','Ustawienia prywatności');
    el.innerHTML = '<strong>Twoja prywatność ma znaczenie</strong><p>Za Twoją zgodą używamy Google Analytics do analizy odwiedzin i kliknięć. Możesz odmówić bez wpływu na korzystanie ze strony. Nie wysyłamy do Analytics danych z formularzy ani informacji o zdrowiu.</p><div class="pbf-actions"><button class="pbf-accept" type="button" data-choice="yes">Akceptuję analitykę</button><button class="pbf-reject" type="button" data-choice="no">Odrzucam</button></div>';
    el.addEventListener('click',function(e){var b=e.target.closest('button[data-choice]');if(b)choose(b.getAttribute('data-choice'));});
    document.body.appendChild(el);
  }
  function init() {
    var settings = document.createElement('button'); settings.id='pbf-privacy-settings'; settings.type='button'; settings.textContent='Ustawienia prywatności';
    settings.addEventListener('click',showBanner); document.body.appendChild(settings);
    var choice = readChoice(); if (choice === 'yes') enableAnalytics(); else if (choice !== 'no') showBanner();
    document.addEventListener('click',function(e){
      if (!enabled || typeof window.gtag !== 'function') return;
      var a = e.target.closest('a[href]'); if (!a) return;
      var href = a.href || '';
      if (/znanylekarz\.pl/i.test(href)) window.gtag('event','booking_click',{link_destination:'znanylekarz',page_path:location.pathname});
      else if (/instagram\.com/i.test(href)) window.gtag('event','social_click',{social_network:'instagram'});
      else if (/tiktok\.com/i.test(href)) window.gtag('event','social_click',{social_network:'tiktok'});
    });
    document.addEventListener('submit',function(e){
      if (!enabled || typeof window.gtag !== 'function') return;
      // Do not transmit email, name, form contents or health information.
      var f=e.target;
      if (f.matches('[data-ebook-form]')) window.gtag('event','ebook_form_submit_attempt');
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
