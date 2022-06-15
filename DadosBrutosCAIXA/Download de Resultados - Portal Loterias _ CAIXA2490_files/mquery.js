function $_global_mquery(){if("undefined"==typeof g_all_modules)g_all_modules={};g_all_modules["mquery.js"]={version:{rmj:16,rmm:0,rup:4873,rpr:1e3}};typeof spWriteProfilerMark=="function"&&spWriteProfilerMark("perfMarkBegin_mquery.js");(function(){if(typeof m$!=="undefined")return;var a=function(){var b=function(b,d,c){var a;if(typeof b!=="undefined"){if(typeof b!=="number")throw TypeError("Starting index must be a number.");a=b}else a=d;if(a<0)a+=c;return a};return{indexOf:function(f,d){for(var c=this.length,e=b(d,0,c),a=e;a<c;++a)if(f===this[a])return a;return-1},lastIndexOf:function(f,d){for(var c=this.length,e=b(d,c-1,c),a=e;a>=0;--a)if(f===this[a])return a;return-1},filter:function(d,c){var b=[];a.forEach.call(this,function(a){d.apply(c,arguments)&&b.push(a)});return b},forEach:function(d,b){for(var c=this.length,a=0;a<c;++a)d.call(b,this[a],a,this)},every:function(d,b){for(var c=this.length,a=0;a<c;++a)if(!d.call(b,this[a],a,this))return false;return true},map:function(d,c){var b=[];a.forEach.call(this,function(){b.push(d.apply(c,arguments))});return b},some:function(d,b){for(var c=this.length,a=0;a<c;++a)if(d.call(b,this[a],a,this))return true;return false}}}(),g={filter:function(c,b){var a={};g.forEach.call(this,function(d,e){if(c.apply(b,arguments))a[d]=e});return a},forEach:function(c,b){for(var a in this)c.call(b,a,this[a],this)},every:function(c,b){for(var a in this)if(!c.call(b,a,this[a],this))return false;return true},map:function(d,c){var b={};for(var a in this)b[a]=d.call(c,a,this[a],this);return b},some:function(c,b){for(var a in this)if(c.call(b,a,this[a],this))return true;return false}};MQueryResultSet=function(){this.push.apply(this,arguments)};MQueryResultSet.prototype=[];MQueryResultSet.prototype.constructor=MQueryResultSet;MQueryResultSet.prototype.append=function(a){if(m$.isNode(a))return this.map(function(b){b.appendChild(a)});else if(m$.isMQueryResultSet(a)){a.forEach(function(a){this.append(a)},this);return this}else if(m$.isString(a))return this.map(function(b){if(typeof b.insertAdjacentHTML!="function")throw new Error("Method insertAdjacentHTML not found.");b.insertAdjacentHTML("beforeend",a)});else throw"Invalid Argument";};MQueryResultSet.prototype.bind=function(a,b){this.forEach(function(d){c.eventBinder(a,d).bind(d,a,b)});return this};MQueryResultSet.prototype.unbind=function(a,b){this.forEach(function(d){c.eventBinder(a,d).unbind(d,a,b)});return this};MQueryResultSet.prototype.trigger=function(b){if(this.length===0)return this;var d=c.eventBinder(b,this[0]).trigger;Array.prototype.splice.call(arguments,0,0,null);var a=arguments;this.forEach(function(b){a[0]=b;d.apply(b,a)});return this};MQueryResultSet.prototype.contains=function(){var a,b=typeof HTMLElement!=="undefined"&&typeof HTMLElement.prototype!=="undefined"&&typeof HTMLElement.prototype.compareDocumentPosition==="function";if(b)a=function(a,b){return(a.compareDocumentPosition(b)&a.DOCUMENT_POSITION_CONTAINED_BY)!==0};else a=function(b,a){return this.contains(a.parentNode)};return function(b){var c=this[0];return typeof b!=="undefined"&&b!==null&&(b===c||a.call(this,c,b))}}();MQueryResultSet.prototype.detach=function(){return this.map(m)};MQueryResultSet.prototype.find=function(b){var a=new MQueryResultSet;this.forEach(function(d){var c;if(b===":root")c=document.querySelectorAll("html");else if(m$.isDefinedAndNotNull(d.querySelectorAll))c=d.querySelectorAll(b);else throw"Unsupported browser.";k(a,c)});return a};MQueryResultSet.prototype.closest=function(b,c){var a=new MQueryResultSet;this.some(function(g){var f=m$(b,c),d=g;while(d!==null){var e=f.indexOf(d);if(e!==-1){a.push(f[e]);return true}else d=d.parentNode}return false});return a};MQueryResultSet.prototype.offset=function(c){if(m$.isUndefined(c)){if(this.length===0)return null;var d=this[0];if(!m$(":root").contains(d))return{left:0,top:0};if(!m$.isDefinedAndNotNull(d.getBoundingClientRect))throw"Unsupported browser.";var b=d.getBoundingClientRect(),a={left:b.left,top:b.top,bottom:b.bottom,right:b.right};if(m$.isNumber(window.pageXOffset))a.left+=window.pageXOffset;else if(m$.isDefinedAndNotNull(document.documentElement)&&m$.isNumber(document.documentElement.scrollLeft))a.left+=document.documentElement.scrollLeft;else throw"Unsupported browser.";if(m$.isNumber(window.pageYOffset))a.top+=window.pageYOffset;else if(m$.isDefinedAndNotNull(document.documentElement)&&m$.isNumber(document.documentElement.scrollTop))a.top+=document.documentElement.scrollTop;else throw"Unsupported browser.";return a}else{this.forEach(function(a){var b=m$(a).offset(),d=function(d){if(c[d]!==b[d]){var e=0;if(a.style[d]===""||a.style[d]==="auto"){a.style[d]="0px";b=m$(a).offset()}else e=CSSUtil.pxToNum(a.style[d]);var f=c[d]-b[d]+e;a.style[d]=String(f)+"px"}};d("left");d("top")});return this}};MQueryResultSet.prototype.one=function(c,d){var a=this,b=function(){a.unbind(c,b);d.apply(this,arguments)};a.bind(c,b);return a};MQueryResultSet.prototype.filter=function(b,c){if(m$.isFunction(b)){var d=a.filter.call(this,b,c);return m$(d)}else if(m$.isString(b))return h(this,b,false);else throw"Invalid Argument";};MQueryResultSet.prototype.not=function(a){return h(this,a,true)};MQueryResultSet.prototype.parent=function(c){var b=this.map(function(a){return a.parentNode}),a;if(m$.isDefined(c))a=b.filter(c);else a=b;return a};MQueryResultSet.prototype.offsetParent=function(){var b=m$(":root"),a=this.map(function(a){return!b.contains(a)?null:a.offsetParent});return a};MQueryResultSet.prototype.parents=function(a){return this.parentsUntil(null,a)};MQueryResultSet.prototype.parentsUntil=function(d,c){var a=new MQueryResultSet;this.forEach(function(c){var b=c.parentNode;while(m$.isElement(b)&&b!==d){a.push(b);b=b.parentNode}});var b;if(m$.isDefined(c))b=a.filter(c);else b=a;return b};MQueryResultSet.prototype.position=function(){if(this.length===0)return null;var a=this[0];return{left:a.style.left,top:a.style.top}};MQueryResultSet.prototype.attr=function(a,d){if(this.length===0)return;var b=this[0];if(m$.isDefinedAndNotNull(d)){b.setAttribute(a,d);return this}else{var c=b.getAttribute(a);return c===null?undefined:c}};MQueryResultSet.prototype.addClass=function(a){if(this.length===1&&a.indexOf(" ")===-1&&this[0].className.indexOf(a)===-1){this[0].className=this[0].className+" "+a;return this}var b=a.split(" ");this.forEach(function(a){m$.forEach(b,function(b){if(b!==""&&a.className.indexOf(b)===-1)a.className=a.className+" "+b});a.className=a.className.trim()});return this};MQueryResultSet.prototype.removeClass=function(b){var a=b.split(" ");this.forEach(function(b){var c=b.className.split(" "),d=m$.filter(c,function(b){return m$.indexOf(a,b)===-1});b.className=d.join(" ")});return this};MQueryResultSet.prototype.css=function(){if(this.length===0)return this;var a;if(arguments.length===1)if(m$.isString(arguments[0])){a=b(arguments[0]);var c=this[0];if(typeof window.getComputedStyle=="function")return getComputedStyle(c,null)[a];else if(typeof c.currentStyle!="undefined")return c.currentStyle[a];else throw"Unsupported browser.";}else{var e=arguments[0];this.forEach(function(c){m$.forEach(e,function(e,d){a=b(e);c.style[a]=d})})}else if(arguments.length===2){a=b(arguments[0]);var d=arguments[1];if(m$.isNumber(d))throw"Values as numbers without units isn't supported in m$ yet.";this.forEach(function(b){b.style[a]=d})}else throw"Invalid arguments.";return this};MQueryResultSet.prototype.remove=function(){!m$.support.domNodeRemoved&&this.map(f);return this.detach()};MQueryResultSet.prototype.children=function(){var a=new MQueryResultSet;this.forEach(function(b){j(a,b.childNodes)});return a};MQueryResultSet.prototype.empty=function(){return this.children().remove()};MQueryResultSet.prototype.first=function(){return m$(this[0])};MQueryResultSet.prototype.data=function(a,c){if(m$.isUndefined(c)&&!m$.isObject(a))return m$.data(this[0],a);var b;this.some(function(d){if(m$.isObject(a))b=m$.extend(m$.data(d),a);else b=m$.data(d,a,c);return m$.isDefinedAndNotNull(b)?true:false});return b};MQueryResultSet.prototype.removeData=function(a){this.forEach(function(b){m$.removeData(b,a)})};MQueryResultSet.prototype.EventuallyDetect_DOMNodeRemovedFromDocument=function(){var b=[],d=false,f=6e4,a="mQuery-EventuallyDetect_DOMNodeRemovedFromDocument_handlers",c=null,e=function(){var d=[];if(c===null)c=m$(":root");m$.forEach(b,function(b){if(c.contains(b))d.push(b);else{var e=b[a];if(m$.isArray(e)){m$.forEach(e,function(a){a()});b[a]=null}}});b=d};return function(c){if(m$.support.domNodeRemovedFromDocument===true)this.one("DOMNodeRemovedFromDocument",c);else{if(!d){d=true;m$.ready(function(){setInterval(e,f)})}this.forEach(function(d){if(m$.isUndefinedOrNull(d[a]))d[a]=[];d[a].push(c);m$.indexOf(b,d)===-1&&b.push(d)})}}}();(function(){var a=function(a){return function(b){var c=this;return typeof b!=="undefined"&&b!==null?this.bind(a,b):this.trigger(a)}};MQueryResultSet.prototype.blur=a("blur");MQueryResultSet.prototype.change=a("change");MQueryResultSet.prototype.click=a("click");MQueryResultSet.prototype.dblclick=a("dblclick");MQueryResultSet.prototype.error=a("error");MQueryResultSet.prototype.focus=a("focus");MQueryResultSet.prototype.focusin=a("focusin");MQueryResultSet.prototype.focusout=a("focusout");MQueryResultSet.prototype.keydown=a("keydown");MQueryResultSet.prototype.keypress=a("keypress");MQueryResultSet.prototype.keyup=a("keyup");MQueryResultSet.prototype.load=a("load");MQueryResultSet.prototype.mousedown=a("mousedown");MQueryResultSet.prototype.mouseenter=a("mouseenter");MQueryResultSet.prototype.mouseleave=a("mouseleave");MQueryResultSet.prototype.mousemove=a("mousemove");MQueryResultSet.prototype.mouseout=a("mouseout");MQueryResultSet.prototype.mouseover=a("mouseover");MQueryResultSet.prototype.mouseup=a("mouseup");MQueryResultSet.prototype.resize=a("resize");MQueryResultSet.prototype.scroll=a("scroll");MQueryResultSet.prototype.select=a("select");MQueryResultSet.prototype.submit=a("submit");MQueryResultSet.prototype.unload=a("unload")})();(function(){if(!("indexOf"in MQueryResultSet.prototype))MQueryResultSet.prototype.indexOf=function(){return a.indexOf.apply(this,arguments)};if(!("lastIndexOf"in MQueryResultSet.prototype))MQueryResultSet.prototype.lastIndexOf=function(){return a.lastIndexOf.apply(this,arguments)};if(!("forEach"in MQueryResultSet.prototype))MQueryResultSet.prototype.forEach=function(){return a.forEach.apply(this,arguments)};if(!("every"in MQueryResultSet.prototype))MQueryResultSet.prototype.every=function(){return a.every.apply(this,arguments)};if("map"in Array.prototype)MQueryResultSet.prototype.map=function(){var a=Array.prototype.map.apply(this,arguments);return m$(a)};else MQueryResultSet.prototype.map=function(){var b=a.map.apply(this,arguments);return m$(b)};if(!("some"in MQueryResultSet.prototype))MQueryResultSet.prototype.some=function(){return a.some.apply(this,arguments)}})();var k=function(c,a){if(typeof a.length==="undefined"||a.length<0)throw"Invalid Argument";for(var d=a.length,b=0;b<d;++b)c.push(a.item(b));return c},h=function(c,d,e){var a=new MQueryResultSet,b=m$(document.body).find(d);c.forEach(function(c){var d=b.indexOf(c)!==-1;e!==d&&a.push(c)});return a},j=function(c,a){if(typeof a.length==="undefined"||a.length<0)throw"Invalid Argument";for(var d=a.length,b=0;b<d;++b)c.push(a[b]);return c},m=function(a){m$.isDefinedAndNotNull(a.parentNode)&&a.parentNode.removeChild(a);return a},f=function(a){m$(a).children().map(f);m$(a).removeData()},b=function(a){return a.replace(/-([a-z])/g,function(b,a){return a.toUpperCase()})},d=function(){var b={},e=0,a="mQuery-objectRef",g="__m$objectRef",d=function(d){var c=d[a];if(m$.isDefinedAndNotNull(c)){delete b[c];delete d[a]}},c=function(c,h){var f=c[a];if(m$.isUndefinedOrNull(c[a])){if(h===true)return;f="m$"+String(e++);c[a]=f;b[f]={};b[f][g]=c;m$.isElement(c)&&m$(c).EventuallyDetect_DOMNodeRemovedFromDocument(function(){d(c)})}return b[f]},i=function(a,d,e){if(m$.isUndefinedOrNull(a)||m$.isNumber(a)||m$.isBoolean(a))return null;var b=c(a);return m$.isUndefinedOrNull(d)?b:m$.isDefined(e)?b[d]=e:b[d]},f=function(e,b){if(m$.isUndefinedOrNull(b))d(e);else{var a=c(e,true);if(m$.isDefinedAndNotNull(a))delete a[b]}},h=function(b){var a=c(b,true);return m$.isDefinedAndNotNull(a)&&!m$.isEmptyObject(a)};return{data:i,removeData:f,hasData:h}}();MQueryEvent=function(e,b){var a=this,d=function(a){return function(){b[a].apply(b,arguments);c()}},c=function(){a.originalEvent=b;m$.extend(a,b);for(var c in a)if(a.hasOwnProperty(c)&&m$.isFunction(a[c]))a[c]=d(c);a.target=m$.isDefined(b.target)?b.target:b.srcElement;a.type=b.type.toLowerCase();if(m$.isDefined(b.clientX)&&m$.isUndefined(b.pageX)){var f=DOM.GetEventCoords(b);a.pageX=f.x;a.pageY=f.y}if(m$.isUndefined(b.relatedTarget))switch(a.type){case"mouseover":case"dragenter":a.relatedTarget=b.fromElement;break;case"mouseout":case"dragexit":a.relatedTarget=b.toElement}if(m$.isUndefined(b.currentTarget))a.currentTarget=e;if(m$.isUndefined(b.preventDefault))a.preventDefault=function(){b.returnValue=false;a.defaultPrevented=true};if(m$.isUndefined(b.stopPropagation))a.stopPropagation=function(){b.cancelBubble=true};switch(a.type){case"keypress":if(b.keyCode===0&&b.which!==0)a.keyCode=b.which;break;case"keydown":case"keyup":a.charCode=0}if(m$.isDefinedAndNotNull(b.which))a.which=b.which;else if(m$.isDefinedAndNotNull(b.keyCode))a.which=b.keyCode;else a.which=b.charCode;delete a.cancelBubble;delete a.returnValue;delete a.srcElement;delete a.fromElement;delete a.toElement;delete a.originalTarget;delete a.layerX;delete a.layerY;delete a.offsetX;delete a.offsetY;delete a.stopImmediatePropagation;delete a.metaKey;delete a.data;delete a.inputMethod;delete a.locale};c()};MQueryEvent.prototype={altKey:false,attrChange:0,attrName:"",bubbles:false,button:0,cancelable:false,ctrlKey:false,defaultPrevented:false,detail:0,eventPhase:0,newValue:"",prevValue:"",relatedNode:undefined,screenX:0,screenY:0,shiftKey:false,view:undefined};MQueryEvent.prototype.constructor=MQueryEvent;var c=function(){var a={CompositionEvents:"CompositionEvents",HTMLEvents:"HTMLEvents",FocusEvents:"FocusEvents",KeyboardEvents:"KeyboardEvents",MouseEvents:"MouseEvents",UIEvents:"UIEvents",MutationEvents:"MutationEvents",MutationNameEvents:"MutationNameEvents",TextEvents:"TextEvents",WheelEvents:"WheelEvents"},d={compositionend:a.CompositionEvents,compositionstart:a.CompositionEvents,compositionupdate:a.CompositionEvents,abort:a.HTMLEvents,blur:a.HTMLEvents,change:a.HTMLEvents,error:a.HTMLEvents,focus:a.HTMLEvents,load:a.HTMLEvents,resize:a.HTMLEvents,scroll:a.HTMLEvents,reset:a.HTMLEvents,select:a.HTMLEvents,submit:a.HTMLEvents,unload:a.HTMLEvents,click:a.MouseEvents,mousemove:a.MouseEvents,mouseout:a.MouseEvents,mouseover:a.MouseEvents,mouseup:a.MouseEvents,mousedown:a.MouseEvents,dblclick:a.MouseEvents,mouseenter:a.MouseEvents,mouseleave:a.MouseEvents,DOMActivate:a.UIEvents,DOMFocusIn:a.UIEvents,DOMFocusOut:a.UIEvents,focusin:a.UIEvents,focusout:a.UIEvents,keydown:a.UIEvents,keypress:a.UIEvents,keyup:a.UIEvents,DOMAttrModified:a.MutationEvents,DOMCharacterDataModified:a.MutationEvents,DOMNodeInserted:a.MutationEvents,DOMNodeInsertedIntoDocument:a.MutationEvents,DOMNodeRemoved:a.MutationEvents,DOMNodeRemovedFromDocument:a.MutationEvents,DOMSubtreeModified:a.MutationEvents,DOMAttributeNameChanged:a.MutationNameEvents,DOMElementNameChanged:a.MutationNameEvents,textInput:a.TextEvents,wheel:a.WheelEvents,contextmenu:a.MouseEvents,beforeunload:a.HTMLEvents},c=function(){var a=function(b){var a=e(b,"eventTypes",{});if(m$.isUndefined(a.vanillaHandlers)||m$.isUndefined(a.wrappedHandlers)){a.vanillaHandlers=[];a.wrappedHandlers=[]}return a},b=function(d,c){var b=a(d);if(m$.indexOf(b.vanillaHandlers,c)===-1){var e=function(g){var b=m$.makeArray(arguments),a;if(m$.isUndefined(g))a=window.event;else a=b.shift();var e=new MQueryEvent(d,a);b.unshift(e);var f=c.apply(d,b);f===false&&e.preventDefault();return f};b.vanillaHandlers.push(c);b.wrappedHandlers.push(e)}var f=m$.indexOf(b.vanillaHandlers,c);return b.wrappedHandlers[f]},c=function(e,d){var b=a(e),c=m$.indexOf(b.vanillaHandlers,d);if(c!==-1){b.vanillaHandlers.splice(c,1);b.wrappedHandlers.splice(c,1)}};return{getAndIncrementRef:function(d,c){var a=b(d,c);if(m$.isUndefined(a.refCount))a.refCount=0;a.refCount++;return a},getAndDecrementRef:function(e,d){var a=b(e,d);if(m$.isNumber(a.refCount)&&a.refCount>0)a.refCount--;else a.refCount=0;a.refCount===0&&c(e,d);return a}}}(),f={bind:function(a,d,e){var b=c.getAndIncrementRef(a,e);if(typeof a.addEventListener!=="undefined")a.addEventListener(d,b,false);else if(typeof a.attachEvent!=="undefined")a.attachEvent("on"+d,b);else throw"Unsupported browser.";},unbind:function(a,d,e){var b=c.getAndDecrementRef(a,e);if(typeof a.removeEventListener!=="undefined")a.removeEventListener(d,b,false);else if(typeof a.detachEvent!=="undefined")a.detachEvent("on"+d,b);else throw"Unsupported browser.";},trigger:function(b,a){if(typeof document.createEvent!=="undefined"){var c=d[a];if(typeof c==="undefined")throw"Unsupported DOM event specified.";var e=document.createEvent(c);e.initEvent(a,true,true);b.dispatchEvent(e)}else if(typeof b.fireEvent!=="undefined")b.fireEvent("on"+a);else throw"Unsupported browser.";}},b=function(a){return e(a,"objEvents",{})},g={bind:function(f,a,d){var c=b(f);if(m$.isUndefinedOrNull(c[a]))c[a]=[];var e=c[a];m$.indexOf(e,d)===-1&&c[a].push(d)},unbind:function(g,a,f){var d=b(g);if(m$.isDefinedAndNotNull(d[a])){var c=d[a],e=m$.indexOf(c,f);e>=0&&c.splice(e,1)}},trigger:function(d,a){var c=b(d);if(m$.isUndefinedOrNull(c[a]))return;var f=c[a],e=Array.prototype.slice.call(arguments,2);m$.forEach(f,function(a){a.apply(d,e)})}},h=function(c,a){var b=m$.isElement(a)||a===window||a===document;return typeof d[c]!=="undefined"&&b?f:g};return{eventBinder:h}}();m$=function(){return m$.initialize.apply(this,arguments)};var l=function(){var a="__m$";return function(c){var b=m$.data(c,a);if(m$.isUndefinedOrNull(b)){b={};m$.data(c,a,b)}return b}}(),e=function(d,a,c){var b=l(d);if(m$.isUndefinedOrNull(b[a])){b[a]=c;m$.data(d,a,c)}return b[a]},i=function(d,h,a,f){if(typeof d==="undefined"||typeof a==="undefined"||f.length<1)throw"Invalid arguments.";for(var e=0;e<f.length;++e){var g=f[e];if(typeof g!=="undefined")for(var c in g){var b=g[c];if(d||typeof a[c]==="undefined")if(typeof b!=="undefined")if(h&&b!==null&&m$.isObject(b)&&!m$.isArray(b)&&!m$.isNode(b)){if(!m$.isObject(a[c]))a[c]={};i(d,h,a[c],[b])}else a[c]=b}}return a};m$.initialize=function(){if(arguments.length>0)if(arguments.length<=2&&m$.isString(arguments[0])){var c=arguments[0],d=arguments[1];return typeof d!=="undefined"?m$(d).find(c):m$(document).find(c)}else if(arguments.length===1){var a=arguments[0];if(m$.isUndefinedOrNull(a))return new MQueryResultSet;else if(m$.isMQueryResultSet(a))return a;else if(m$.isNode(a)||a===window)return new MQueryResultSet(a);else if(m$.isArray(a)){var b=new MQueryResultSet;MQueryResultSet.apply(b,a);return b}else return new MQueryResultSet(a)}return new MQueryResultSet};m$.throttle=function(g,f,c){var b=false,a=false,e=this,d=function(){if(!b||m$.isFunction(c)&&c()){b=true;setTimeout(function(){var c=a;b=a=false;c&&d.apply(e,arguments)},f);g.apply(e,arguments)}else a=true};return d};m$.extend=function(){var b=m$.makeArray(arguments),a=b.shift(),c=false;if(m$.isBoolean(a)){c=a;a=b.shift()}if(b.length===0){b=[a];a=m$}return i(true,c,a,b)};m$.makeArray=function(a){return Array.prototype.slice.call(a,0)};m$.isDefined=function(a){return typeof a!=="undefined"};m$.isNotNull=function(a){return a!==null};m$.isUndefined=function(a){return typeof a==="undefined"};m$.isNull=function(a){return a===null};m$.isUndefinedOrNull=function(a){return a==null};m$.isDefinedAndNotNull=function(a){return a!=null};m$.isString=function(a){return typeof a==="string"};m$.isBoolean=function(a){return typeof a==="boolean"};m$.isFunction=function(a){return typeof a==="function"};m$.isArray=m$.isFunction(Array.isArray)?Array.isArray:function(a){return Object.prototype.toString.call(a)==="[object Array]"};m$.isNode=function(){return typeof Node==="object"?function(a){return a instanceof Node}:function(a){return m$.isDefinedAndNotNull(a)&&m$.isDefined(a.nodeType)&&m$.isNumber(a.nodeType)&&typeof a.nodeName==="string"}}();m$.isElement=function(){return typeof HTMLElement==="object"?function(a){return a instanceof HTMLElement}:function(a){return m$.isNode(a)&&a.nodeType===1}}();m$.isMQueryResultSet=function(a){return a instanceof MQueryResultSet};m$.isNumber=function(a){return typeof a==="number"};m$.isObject=function(a){return m$.isNotNull(a)&&typeof a==="object"};m$.isEmptyObject=function(a){for(var b in a)return true;return false};m$.isReady=false;IE8Support.attachDOMContentLoaded(function(){m$.isReady=true});m$.ready=function(a){if(m$.isReady)a();else IE8Support.attachDOMContentLoaded(a)};m$.contains=function(b,a){return b!==a&&m$.isDefinedAndNotNull(b)&&m$.isDefinedAndNotNull(a)&&m$(b).contains(a)};m$.proxy=function(b,a){if(typeof a==="undefined")throw"Invalid context";return function(){b.apply(a,arguments)}};m$.support={};m$.support.domAttrModified=false;m$.support.domSubtreeModified=false;m$.support.domNodeRemoved=false;m$.support.domNodeRemovedFromDocument=false;m$.every=function(){return false};m$.filter=function(){return null};m$.forEach=function(){};m$.indexOf=function(){return 0};m$.lastIndexOf=function(){return 0};m$.map=function(){return null};m$.some=function(){return false};m$.data=d.data;m$.removeData=d.removeData;m$.hasData=d.hasData;(function(){var b=function(b){return function(){var d=m$.makeArray(arguments),c=d.shift();if(m$.isUndefinedOrNull(c))throw"Invalid argument specified";if(m$.isArray(c))return b in c?c[b].apply(c,d):a[b].apply(c,d);else if(m$.isObject(c))return g[b].apply(c,d);throw"Invalid argument";}};(function(){for(var c in a)if(a.hasOwnProperty(c))m$[c]=b(c)})()})();(function(){var a=document.createElement("div");a.style.display="none";var b=document.createElement("p");m$(a).one("DOMAttrModified",function(){m$.support.domAttrModified=true});a.id="face";m$(a).one("DOMSubtreeModified",function(){m$.support.domSubtreeModified=true});a.appendChild(b);m$.ready(function(){document.body.appendChild(a);m$(a).one("DOMNodeRemovedFromDocument",function(){m$.support.domNodeRemovedFromDocument=true});document.body.removeChild(a)});m$(b).one("DOMNodeRemoved",function(){m$.support.domNodeRemoved=true});a.removeChild(b)})()})();typeof spWriteProfilerMark=="function"&&spWriteProfilerMark("perfMarkEnd_mquery.js")}var m$,MQueryResultSet,MQueryEvent;$_global_mquery();