(self.webpackJsonp=self.webpackJsonp||[]).push([[104],{174:function(e,t,r){"use strict";var i=r(0);function o(e){var t,r=l(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function a(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function n(e){return e.decorators&&e.decorators.length}function s(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function c(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function l(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}let d=function(e,t,r,i){var d=function(){var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach(function(r){t.forEach(function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)},this)},this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach(function(i){t.forEach(function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}},this)},this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach(function(e){this.addElementPlacement(e,o)},this),e.forEach(function(e){if(!n(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)},this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,o[a])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var s=n+1;s<e.length;s++)if(e[n].key===e[s].key&&e[n].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()).map(function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t},this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=l(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){var t=this.toElementDescriptor(e),r=c(e,"finisher"),i=this.toElementDescriptors(e.extras);return{element:t,finisher:r,extras:i}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=c(e,"finisher"),i=this.toElementDescriptors(e.elements);return{elements:i,finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}();if(i)for(var p=0;p<i.length;p++)d=i[p](d);var u=t(function(e){d.initializeInstanceElements(e,f.elements)},r),f=d.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===c.key&&e.placement===c.placement},i=0;i<e.length;i++){var o,c=e[i];if("method"===c.kind&&(o=t.find(r)))if(s(c.descriptor)||s(o.descriptor)){if(n(c)||n(o))throw new ReferenceError("Duplicated methods ("+c.key+") can't be decorated.");o.descriptor=c.descriptor}else{if(n(c)){if(n(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+c.key+").");o.decorators=c.decorators}a(c,o)}else t.push(c)}return t}(u.d.map(o)),e);return d.initializeClassElements(u.F,f.elements),d.runClassFinishers(u.F,f.finishers)}(null,function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[Object(i.g)()],key:"header",value:void 0},{kind:"get",static:!0,key:"styles",value:function(){return i.c`
      :host {
        background: var(
          --ha-card-background,
          var(--paper-card-background-color, white)
        );
        border-radius: var(--ha-card-border-radius, 2px);
        box-shadow: var(
          --ha-card-box-shadow,
          0 2px 2px 0 rgba(0, 0, 0, 0.14),
          0 1px 5px 0 rgba(0, 0, 0, 0.12),
          0 3px 1px -2px rgba(0, 0, 0, 0.2)
        );
        color: var(--primary-text-color);
        display: block;
        transition: all 0.3s ease-out;
        position: relative;
      }

      .card-header,
      :host ::slotted(.card-header) {
        color: var(--ha-card-header-color, --primary-text-color);
        font-family: var(--ha-card-header-font-family, inherit);
        font-size: var(--ha-card-header-font-size, 24px);
        letter-spacing: -0.012em;
        line-height: 32px;
        padding: 24px 16px 16px;
        display: block;
      }

      :host ::slotted(.card-content:not(:first-child)),
      slot:not(:first-child)::slotted(.card-content) {
        padding-top: 0px;
        margin-top: -8px;
      }

      :host ::slotted(.card-content) {
        padding: 16px;
      }

      :host ::slotted(.card-actions) {
        border-top: 1px solid #e8e8e8;
        padding: 5px 16px;
      }
    `}},{kind:"method",key:"render",value:function(){return i.f`
      ${this.header?i.f`
            <div class="card-header">${this.header}</div>
          `:i.f``}
      <slot></slot>
    `}}]}},i.a);customElements.define("ha-card",d)},177:function(e,t,r){"use strict";r.d(t,"a",function(){return a});r(107);const i=customElements.get("iron-icon");let o=!1;class a extends i{constructor(...e){var t,r,i;super(...e),i=void 0,(r="_iconsetName")in(t=this)?Object.defineProperty(t,r,{value:i,enumerable:!0,configurable:!0,writable:!0}):t[r]=i}listen(e,t,i){super.listen(e,t,i),o||"mdi"!==this._iconsetName||(o=!0,r.e(85).then(r.bind(null,208)))}}customElements.define("ha-icon",a)},193:function(e,t,r){"use strict";var i=r(0),o=(r(211),r(194));function a(e){var t,r=d(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function n(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function s(e){return e.decorators&&e.decorators.length}function c(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function l(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function d(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t,r){return(p="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=u(e)););return e}(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(r):o.value}})(e,t,r||e)}function u(e){return(u=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}const f=customElements.get("mwc-switch");!function(e,t,r,i){var o=function(){var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach(function(r){t.forEach(function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)},this)},this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach(function(i){t.forEach(function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}},this)},this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach(function(e){this.addElementPlacement(e,o)},this),e.forEach(function(e){if(!s(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)},this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,o[a])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var s=n+1;s<e.length;s++)if(e[n].key===e[s].key&&e[n].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()).map(function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t},this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=d(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){var t=this.toElementDescriptor(e),r=l(e,"finisher"),i=this.toElementDescriptors(e.extras);return{element:t,finisher:r,extras:i}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=l(e,"finisher"),i=this.toElementDescriptors(e.elements);return{elements:i,finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}();if(i)for(var p=0;p<i.length;p++)o=i[p](o);var u=t(function(e){o.initializeInstanceElements(e,f.elements)},r),f=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===a.key&&e.placement===a.placement},i=0;i<e.length;i++){var o,a=e[i];if("method"===a.kind&&(o=t.find(r)))if(c(a.descriptor)||c(o.descriptor)){if(s(a)||s(o))throw new ReferenceError("Duplicated methods ("+a.key+") can't be decorated.");o.descriptor=a.descriptor}else{if(s(a)){if(s(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+a.key+").");o.decorators=a.decorators}n(a,o)}else t.push(a)}return t}(u.d.map(a)),e);o.initializeClassElements(u.F,f.elements),o.runClassFinishers(u.F,f.finishers)}([Object(i.d)("ha-switch")],function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[Object(i.h)("slot")],key:"_slot",value:void 0},{kind:"method",key:"firstUpdated",value:function(){p(u(r.prototype),"firstUpdated",this).call(this),this.style.setProperty("--mdc-theme-secondary","var(--switch-checked-color)"),this.classList.toggle("slotted",Boolean(this._slot.assignedNodes().length))}},{kind:"get",static:!0,key:"styles",value:function(){return[o.a,i.c`
        :host {
          display: flex;
          flex-direction: row;
          align-items: center;
        }
        .mdc-switch.mdc-switch--checked .mdc-switch__thumb {
          background-color: var(--switch-checked-button-color);
          border-color: var(--switch-checked-button-color);
        }
        .mdc-switch.mdc-switch--checked .mdc-switch__track {
          background-color: var(--switch-checked-track-color);
          border-color: var(--switch-checked-track-color);
        }
        .mdc-switch:not(.mdc-switch--checked) .mdc-switch__thumb {
          background-color: var(--switch-unchecked-button-color);
          border-color: var(--switch-unchecked-button-color);
        }
        .mdc-switch:not(.mdc-switch--checked) .mdc-switch__track {
          background-color: var(--switch-unchecked-track-color);
          border-color: var(--switch-unchecked-track-color);
        }
        :host(.slotted) .mdc-switch {
          margin-right: 24px;
        }
      `]}}]}},f)},231:function(e,t,r){"use strict";r(107);var i=r(177);customElements.define("ha-icon-next",class extends i.a{connectedCallback(){super.connectedCallback(),setTimeout(()=>{this.icon="ltr"===window.getComputedStyle(this).direction?"hass:chevron-right":"hass:chevron-left"},100)}})},286:function(e,t,r){"use strict";r(107),r(181),r(140),r(174),r(231);var i=r(0);function o(e){var t,r=l(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function a(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function n(e){return e.decorators&&e.decorators.length}function s(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function c(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function l(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}const d=[{page:"ais_dom_config_update",caption:"Oprogramowanie bramki",description:"Aktualizacja systemu i synchronizacja bramki z Portalem Integratora"},{page:"ais_dom_config_wifi",caption:"Sieć WiFi",description:"Ustawienia połączenia z siecią WiFi"},{page:"ais_dom_config_display",caption:"Ekran",description:"Ustawienia ekranu"},{page:"ais_dom_config_tts",caption:"Głos asystenta",description:"Ustawienia głosu asystenta"},{page:"ais_dom_config_night",caption:"Tryb nocny",description:"Ustawienie godzin, w których asystent ma działać ciszej"},{page:"ais_dom_config_remote",caption:"Zdalny dostęp",description:"Konfiguracja zdalnego dostępu do bramki"},{page:"ais_dom_config_power",caption:"Zatrzymanie bramki",description:"Restart lub wyłączenie bramki"}];!function(e,t,r,i){var d=function(){var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach(function(r){t.forEach(function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)},this)},this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach(function(i){t.forEach(function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var a="static"===o?e:r;this.defineClassElement(a,t)}},this)},this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach(function(e){this.addElementPlacement(e,o)},this),e.forEach(function(e){if(!n(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)},this),!t)return{elements:r,finishers:i};var a=this.decorateConstructor(r,t);return i.push.apply(i,a.finishers),a.finishers=i,a},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,a=o.length-1;a>=0;a--){var n=t[e.placement];n.splice(n.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,o[a])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),a=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==a.finisher&&r.push(a.finisher),void 0!==a.elements){e=a.elements;for(var n=0;n<e.length-1;n++)for(var s=n+1;s<e.length;s++)if(e[n].key===e[s].key&&e[n].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[n].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e))return Array.from(e)}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()).map(function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t},this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=l(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var a={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),a.initializer=e.initializer),a},toElementFinisherExtras:function(e){var t=this.toElementDescriptor(e),r=c(e,"finisher"),i=this.toElementDescriptors(e.extras);return{element:t,finisher:r,extras:i}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=c(e,"finisher"),i=this.toElementDescriptors(e.elements);return{elements:i,finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}();if(i)for(var p=0;p<i.length;p++)d=i[p](d);var u=t(function(e){d.initializeInstanceElements(e,f.elements)},r),f=d.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===c.key&&e.placement===c.placement},i=0;i<e.length;i++){var o,c=e[i];if("method"===c.kind&&(o=t.find(r)))if(s(c.descriptor)||s(o.descriptor)){if(n(c)||n(o))throw new ReferenceError("Duplicated methods ("+c.key+") can't be decorated.");o.descriptor=c.descriptor}else{if(n(c)){if(n(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+c.key+").");o.decorators=c.decorators}a(c,o)}else t.push(c)}return t}(u.d.map(o)),e);d.initializeClassElements(u.F,f.elements),d.runClassFinishers(u.F,f.finishers)}([Object(i.d)("ha-config-ais-dom-navigation")],function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[Object(i.g)()],key:"hass",value:void 0},{kind:"field",decorators:[Object(i.g)()],key:"showAdvanced",value:void 0},{kind:"method",key:"render",value:function(){return i.f`
      <ha-card>
        ${d.map(({page:e,caption:t,description:r})=>i.f`
              <a href=${`/config/${e}`}>
                <paper-item>
                  <paper-item-body two-line=""
                    >${`${t}`}
                    <div secondary>${`${r}`}</div>
                  </paper-item-body>
                  <ha-icon-next></ha-icon-next>
                </paper-item>
              </a>
            `)}
      </ha-card>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return i.c`
      a {
        text-decoration: none;
        color: var(--primary-text-color);
      }
    `}}]}},i.a)},725:function(e,t,r){"use strict";r.r(t);r(217),r(147);var i=r(4),o=r(29);r(148),r(93),r(286),r(193);customElements.define("ha-config-ais-dom-config-update",class extends o.a{static get template(){return i.a`
      <style include="iron-flex ha-style">
        .content {
          padding-bottom: 32px;
        }
        .border {
          margin: 32px auto 0;
          border-bottom: 1px solid rgba(0, 0, 0, 0.12);
          max-width: 1040px;
        }
        .narrow .border {
          max-width: 640px;
        }
        .center-container {
          @apply --layout-vertical;
          @apply --layout-center-center;
          height: 70px;
        }
        table {
          width: 100%;
        }

        td:first-child {
          width: 33%;
        }

        .validate-container {
          @apply --layout-vertical;
          @apply --layout-center-center;
          min-height: 140px;
        }

        .validate-result {
          color: var(--google-green-500);
          font-weight: 500;
        }

        .config-invalid .text {
          color: var(--google-red-500);
          font-weight: 500;
        }

        .config-invalid {
          text-align: center;
          margin-top: 20px;
        }

        .validate-log {
          white-space: pre-wrap;
          direction: ltr;
        }
      </style>

      <hass-subpage header="Konfiguracja bramki AIS dom">
        <div class$="[[computeClasses(isWide)]]">
          <ha-config-section is-wide="[[isWide]]">
            <span slot="header">Oprogramowanie bramki</span>
            <span slot="introduction"
              >Możesz zaktualizować system do najnowszej wersji, wykonać kopię
              zapasową ustawień i zsynchronizować bramkę z Portalem
              Integratora</span
            >
            <ha-card header="Wersja systemu Asystent domowy">
              <div class="card-content">
                [[aisVersionInfo]]
                <div>
                  <div style="margin-top:30px;" id="ha-switch-id">
                    <ha-switch
                      checked="{{autoUpdateMode}}"
                      on-change="changeAutoUpdateMode"
                      style="position: absolute; right: 20px;"
                    ></ha-switch
                    ><span
                      ><h3>
                        Autoaktualizacja
                        <iron-icon icon="[[aisAutoUpdateIcon]]"></iron-icon></h3
                    ></span>
                  </div>
                </div>

                <div style="display: inline-block;">
                  <div>
                    [[aisAutoUpdateInfo]]
                  </div>
                  <div style="margin-top: 15px;">
                    Aktualizacje dostarczają najnowsze funkcjonalności oraz
                    poprawki zapewniające bezpieczeństwo i stabilność działania
                    systemu.
                    <table style="margin-top: 10px;">
                      <template
                        is="dom-repeat"
                        items="[[aisAutoUpdatFullInfo]]"
                      >
                        <tr>
                          <td>[[item.name]]</td>
                          <td>[[item.value]]</td>
                          <td>[[item.new_value]]</td>
                          <td><iron-icon icon="[[item.icon]]"></iron-icon></td>
                        </tr>
                      </template>
                    </table>
                  </div>
                </div>
                <div class="center-container">
                  <ha-call-service-button
                    class="warning"
                    hass="[[hass]]"
                    domain="ais_updater"
                    service="execute_upgrade"
                    service-data="[[aisUpdateSystemData]]"
                    >[[aisButtonVersionCheckUpgrade]]
                  </ha-call-service-button>
                </div>
              </div>
            </ha-card>

            <ha-card header="Kopia konfiguracji Bramki">
              <div class="card-content">
                W tym miejscu możesz, sprawdzić poprawność ustawień bramki,
                wykonać jej kopię i przesłać ją do portalu integratora. <b>Uwaga,
                ponieważ konfiguracja może zawierać hasła i tokeny dostępu do
                usług, zalecamy zaszyfrować ją hasłem</b>, Gdy kopia jest
                zabezpieczona hasłem, to można ją otworzyć/przywrócić tylko po
                podaniu hasła.
                <h2>
                  Nowa kopia ustawień
                  <iron-icon icon="mdi:cloud-upload-outline"></iron-icon>
                </h2>
                Przed wykonaniem nowej kopii usatawień sprawdz poprawność
                konfiguracji
                <div style="border-bottom: 1px solid white;">
                  <template is="dom-if" if="[[!validateLog]]">
                    <div class="validate-container">
                      <div class="validate-result" id="result">
                        [[backupInfo]]
                      </div>
                      <template is="dom-if" if="[[!validating]]">
                        <div class="config-invalid">
                          <span class="text">
                            [[backupError]]
                          </span>
                        </div>
                        <template
                          is="dom-if"
                          if="[[_isEqualTo(backupStep, '1')]]"
                        >
                          <paper-input
                            placeholder="hasło"
                            no-label-float=""
                            type="password"
                            id="password1"
                          ></paper-input>
                        </template>
                        <mwc-button raised="" on-click="doBackup">
                          <template
                            is="dom-if"
                            if="[[_isEqualTo(backupStep, '0')]]"
                          >
                            Sprawdz konfigurację
                          </template>
                          <template
                            is="dom-if"
                            if="[[_isEqualTo(backupStep, '1')]]"
                          >
                            Wykonaj kopie konfiguracji
                          </template>
                        </mwc-button>
                      </template>
                      <template is="dom-if" if="[[validating]]">
                        <paper-spinner active=""></paper-spinner>
                      </template>
                    </div>
                  </template>
                  <template is="dom-if" if="[[validateLog]]">
                    <div class="config-invalid">
                      <mwc-button raised="" on-click="doBackup">
                        Popraw i sprawdz ponownie
                      </mwc-button>
                    </div>
                    <p></p>
                    <div id="configLog" class="validate-log">
                      [[validateLog]]
                    </div>
                  </template>
                </div>

                <template is="dom-if" if="[[isBackupValid]]">
                  <h2>
                    Przywracanie ustawień
                    <iron-icon icon="mdi:backup-restore"></iron-icon>
                  </h2>
                  <div class="validate-container">
                    <table style="margin-top: 40px; margin-bottom: 10px;">
                      <template is="dom-repeat" items="[[aisBackupFullInfo]]">
                        <tr>
                          <td>[[item.name]]</td>
                          <td>[[item.value]]</td>
                          <td>[[item.new_value]]</td>
                          <td><iron-icon icon="[[item.icon]]"></iron-icon></td>
                        </tr>
                      </template>
                    </table>
                      <div class="validate-container">
                        <div class="validate-result" id="result">
                          [[restoreInfo]]
                        </div>
                        <template is="dom-if" if="[[!validating]]">
                        <div class="config-invalid">
                          <span class="text">
                            [[restoreError]]
                          </span>
                        </div>
                        <paper-input
                          placeholder="hasło"
                          no-label-float=""
                          type="password"
                          id="password2"
                        ></paper-input>
                        <mwc-button raised="" on-click="restoreBackup">
                          Przywróć konfigurację z kopii
                        </mwc-button>
                      </div>
                    </template>
                    <template is="dom-if" if="[[validating]]">
                      <paper-spinner active=""></paper-spinner>
                    </template>
                  </div>
                </template>
              </div>
            </ha-card>

            <ha-card header="Synchronizacja z Portalem Integratora">
              <div class="card-content">
                Jeśli ostatnio wprowadzałeś zmiany w Portalu Integratora, takie
                jak dodanie nowych typów audio czy też dostęp do zewnętrznych
                serwisów, to przyciskiem poniżej możesz uruchomić natychmiastowe
                pobranie tych zmian na bramkę bez czekania na automatyczną
                synchronizację.
                <div class="center-container">
                  <ha-call-service-button
                    class="warning"
                    hass="[[hass]]"
                    domain="script"
                    service="ais_cloud_sync"
                    >Synchronizuj z Portalem Integratora
                  </ha-call-service-button>
                </div>
              </div>
            </ha-card>
          </ha-config-section>
        </div>
      </hass-subpage>
    `}static get properties(){return{hass:Object,isWide:Boolean,aisVersionInfo:{type:String,computed:"_computeAisVersionInfo(hass)"},aisBackupInfo:{type:String,computed:"_computeAisBackupInfo(hass)"},aisAutoUpdateInfo:{type:String},aisAutoUpdateIcon:{type:String},aisAutoUpdatFullInfo:{type:Array,value:[]},aisBackupFullInfo:{type:Array,value:[]},aisButtonVersionCheckUpgrade:{type:String,computed:"_computeAisButtonVersionCheckUpgrade(hass)"},aisUpdateSystemData:{type:Object,value:{say:!0}},autoUpdateMode:{type:Boolean,computed:"_computeAutoUpdateMode(hass)"},validating:{type:Boolean,value:!1},backupStep:{type:String,value:"0",computed:"_computeAisBackupStep(hass)"},validateLog:{type:String,value:""},backupInfo:{type:String,value:""},backupError:{type:String,value:""},restoreInfo:{type:String,value:""},restoreError:{type:String,value:""},isBackupValid:{type:Boolean,value:null}}}ready(){super.ready(),this.hass.callService("ais_cloud","set_backup_step",{step:"0"}),this.hass.callService("ais_cloud","get_backup_info")}computeClasses(e){return e?"content":"content narrow"}_computeAisVersionInfo(e){var t=e.states["sensor.version_info"],r=t.attributes;return this.aisAutoUpdatFullInfo=[],"update_check_time"in r&&this.aisAutoUpdatFullInfo.push({name:"Sprawdzono o",value:r.update_check_time,icon:""}),"update_status"in r&&this.aisAutoUpdatFullInfo.push({name:"Status",value:this.getVersionName(r.update_status),icon:this.getVersionIcon(r.update_status)}),"dom_app_current_version"in r&&this.aisAutoUpdatFullInfo.push({name:"Asystent domowy",value:r.dom_app_current_version,new_value:r.dom_app_newest_version,icon:r.reinstall_dom_app?"hass:alert":"hass:check"}),"android_app_current_version"in r&&this.aisAutoUpdatFullInfo.push({name:"Android",value:r.android_app_current_version,new_value:r.android_app_newest_version,icon:r.reinstall_android_app?"hass:alert":"hass:check"}),"linux_apt_current_version"in r&&this.aisAutoUpdatFullInfo.push({name:"Linux",value:r.linux_apt_current_version,new_value:r.linux_apt_newest_version,icon:r.reinstall_linux_apt?"hass:alert":"hass:check"}),t.state}_computeAisBackupStep(e){var t=e.states["sensor.aisbackupinfo"];return"0"===t.state&&(this.validating=!1),t.state}_computeAisBackupInfo(e){var t=e.states["sensor.aisbackupinfo"],r=t.attributes;return this.aisBackupFullInfo=[],this.isBackupValid=!1,this.backupInfo=r.backup_info,this.backupError=r.backup_error,this.restoreInfo=r.restore_info,this.restoreError=r.restore_error,"file_size"in r&&(this.isBackupValid=!!r.file_name,this.aisBackupFullInfo.push({name:"Kopia zapasowa",value:r.file_name,new_value:r.file_size,icon:"mdi:check"})),t.state}getVersionName(e){var t=e;return"checking"===e?t="Sprawdzanie":"outdated"===e?t="Nieaktualny":"downloading"===e?t="Pobieranie":"installing"===e?t="Instalowanie":"updated"===e?t="Aktualny":"unknown"===e?t="Nieznany":"restart"===e&&(t="Restartowanie"),t}getVersionIcon(e){var t="";return"checking"===e?t="mdi:cloud-sync":"outdated"===e?t="":"downloading"===e?t="mdi:progress-download":"installing"===e?t="mdi:progress-wrench":"updated"===e?t="mdi:emoticon-happy-outline":"unknown"===e?t="mdi:help-circle-outline":"restart"===e&&(t="mdi:restart-alert"),t}_computeAisButtonVersionCheckUpgrade(e){var t=e.states["sensor.version_info"].attributes;return t.reinstall_dom_app||t.reinstall_android_app||t.reinstall_linux_apt?"outdated"===t.update_status?"Zainstaluj teraz aktualizację":"unknown"===t.update_status?"Spróbuj ponownie":"Aktualizacja -> "+this.getVersionName(t.update_status):"Sprawdz dostępność aktualizacji"}_computeAutoUpdateMode(e){return"off"===e.states["input_boolean.ais_auto_update"].state?(this.aisAutoUpdateIcon="mdi:sync-off",this.aisAutoUpdateInfo="Możesz aktualizować system samodzielnie w dogodnym dla Ciebie czasie lub włączyć aktualizację automatyczną.",!1):(this.aisAutoUpdateIcon="mdi:sync",this.aisAutoUpdateInfo="Codziennie sprawdzimy i automatycznie zainstalujemy dostępne aktualizacje.",!0)}_isEqualTo(e,t){return e===t}changeAutoUpdateMode(){this.hass.callService("input_boolean","toggle",{entity_id:"input_boolean.ais_auto_update"})}doBackup(){if("0"===this.backupStep)this.validating=!0,this.validateLog="",this.hass.callApi("POST","config/core/check_config").then(e=>{this.validating=!1;var t="valid"===e.result?"1":"0";"0"===t?(this.hass.callService("ais_cloud","set_backup_step",{step:t,backup_error:"Konfiguracja niepoprawana"}),this.validateLog=e.errors):(this.hass.callService("ais_cloud","set_backup_step",{step:t,backup_info:"Konfiguracja poprawna można wykonać kopie"}),this.validateLog="")});else{this.validating=!0,this.validateLog="";var e=this.shadowRoot.getElementById("password1").value;this.hass.callService("ais_cloud","do_backup",{password:e})}}restoreBackup(){this.validating=!0,this.validateLog="";var e=this.shadowRoot.getElementById("password2").value;this.hass.callService("ais_cloud","restore_backup",{password:e})}})}}]);
//# sourceMappingURL=chunk.4bfb6c77fe9913603aff.js.map