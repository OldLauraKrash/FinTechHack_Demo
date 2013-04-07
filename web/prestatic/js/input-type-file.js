// custom upload input
function initCustomFile() {
	var inputs = document.getElementsByTagName('input');
	for (var i= 0; i < inputs.length; i++) {
		if(inputs[i].className.indexOf('file-input-area') != -1) {
			new customFileUpload(inputs[i]);
		}
	}
}

// custom file input module
function customFileUpload(obj, opt) {
	if(obj) {
		this.options = {
			jsActiveClass:'file-input-js-active',
			fakeClass:'file-input-value',
			hoverClass:'hover'
		}
		this.fileInput = obj;
		this.fileInput.custClass = this;
		this.init();
	}
}
customFileUpload.prototype = {
	init: function() {
		this.getElements();
		this.setStyles();
		this.addEvents();
	},
	getElements: function() {
		this.fileInputParent = this.fileInput.parentNode;
		this.fileInputParent.className += ' ' + this.options.jsActiveClass;
		var tmpInputs = this.fileInput.parentNode.getElementsByTagName('input');
		for(var i = 0; i < tmpInputs.length; i++) {
			if(tmpInputs[i].className.indexOf(this.options.fakeClass) != -1) {
				this.fakeInput = tmpInputs[i];
				this.fakeInput.readOnly = true;
				break;
			}
		}
	},
	getFileName: function(){
		return this.fileInput.value.replace(/^[\s\S]*(?:\\|\/)([\s\S^\\\/]*)$/g, "$1");
	},
	setStyles: function() {
		// IE styling fix
		if((/(MSIE)/gi).test(navigator.userAgent)) {
			this.tmpNode = document.createElement('span');
			this.fileInputParent.insertBefore(this.tmpNode,this.fileInput);
			this.fileInputParent.insertBefore(this.fileInput,this.tmpNode);
			this.fileInputParent.removeChild(this.tmpNode);
		}
		this.fileInput.style.opacity = 0;
		this.fileInput.style.filter = 'alpha(opacity=0)';
	},
	addEvents: function() {
		this.fileInput.onchange = this.bind(this.updateTitle,this);
		this.fileInput.onmouseover = this.bind(function(){
			this.fileInputParent.className += ' ' + this.options.hoverClass;
		},this);
		this.fileInput.onmouseout = this.bind(function(){
			this.fileInputParent.className = this.fileInputParent.className.replace(' '+this.options.hoverClass,'');
		},this);
	},
	updateTitle: function() {
		if(this.fakeInput) {
			this.fakeInput.value = this.getFileName();
		}
	},
	bind: function(func, scope) {
		return function() {
			return func.apply(scope, arguments);
		}
	}
}

if (window.addEventListener) window.addEventListener("load", initCustomFile, false);
else if (window.attachEvent) window.attachEvent("onload", initCustomFile);