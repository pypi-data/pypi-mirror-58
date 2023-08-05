// Adds a button to hide the input part of the currently selected cells

define([
  'jquery',
  'base/js/namespace',
  'base/js/events',
], function (
  $,
  Jupyter,
  events,
) {
  "use strict";
  // NOTE: all the functions should be idempotent, i.e on multiple load of same
  // function should have same behaviour
  function injectScript(src) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.async = true;
      script.src = src;
      script.addEventListener('load', resolve);
      script.addEventListener('error', () => reject('Error loading script.'));
      script.addEventListener('abort', () => reject('Script loading aborted.'));
      document.head.appendChild(script);
    });
  }

  function initlogrocket() {
    injectScript('https://cdn.lr-ingest.io/LogRocket.min.js')
      .then(() => {
        window.LogRocket && window.LogRocket.init('colaberry/refactored');
        LogRocket.identify(/user\/([^/]+)/.exec(Jupyter.notebook.base_url)[1]);
      }).catch(error => {
        console.log(error);
      });
  }

  function initgoogleanalytics() {
    injectScript("https://www.googletagmanager.com/gtag/js?id=UA-50774814-6")
      .then(() => {
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-50774814-6');
      }).catch(error => {
        console.log(error);
      });
  }

  function initlogs() {
    initlogrocket();
    initgoogleanalytics();
  }

  var load_extension = function () {
    if (Jupyter.notebook !== undefined && Jupyter.notebook._fully_loaded) {
      initlogs();
    }
    events.on("notebook_loaded.Notebook", initlogs);
  };

  return {
    load_extension: load_extension
  };
});
