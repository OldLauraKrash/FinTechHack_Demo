$(document).ready(function(){
	$('.slide-frame').slider({
		range: "min",
		value: 30,
		min: 1,
		max: 100,
		step:1,
		slide: function( event, ui ) {
			$(".slide-frame .ui-slider-handle").text( ui.value+'K' );
		}
	});
	$(".slide-frame .ui-slider-handle").text($('.slide-frame').slider( "value" )+'K' );
	popupbg();
	/*
	$('#btn-popup1').click(function(){
		popupbg();
		$('#popup1').css({"left": "-9999px"});
		$('#popup1').show();
		windowScroll($('#popup1 .popup').height());
		$('#popup1').hide();
		$('#popup1').css({"left": "0"});
		$('#popup1 .popup').css('top',wScroll);
		$('#popup1').fadeIn(200);
		return false;
	});
	*/
	$('#popup1 .btn-form input').click(function(){
		$('#popup1').fadeOut(300, function(){
			$('#popup1').css({"left": "-9999px"});
			$('#popup1').height(0);
			$('#popup1').show();
		});
		popupbg();
		$('#popup2').css({"left": "-9999px"});
		$('#popup2').show();
		windowScroll($('#popup2 .popup').height());
		$('#popup2').hide();
		$('#popup2').css({"left": "0"});
		$('#popup2 .popup').css('top',wScroll);
		$('#popup2').fadeIn(200);
		return false;
	});
	
	/*
	$('#btn-popup2').click(function(){
		popupbg();
		$('#popup3').css({"left": "-9999px"});
		$('#popup3').show();
		windowScroll($('#popup3 .popup').height());
		$('#popup3').hide();
		$('#popup3').css({"left": "0"});
		$('#popup3 .popup').css('top',wScroll);
		$('#popup3').fadeIn(200);
		return false;
	});
	*/
	$('.popup-holder .bg').click(function(){
		$(this).parents('.popup-holder').fadeOut(300, function(){
			$('.popup-holder').css({"left": "-9999px"});
			$('.popup-holder').height(0);
			$('.popup-holder').show();
		});
		return false;
	});
	$('.link-holder.link-holder-indent .btn-status').not('.decline').click(function(){
		$(this).closest('.link-holder').toggleClass('active');
		return false;
	});
	$(document).click(function(event) {
		if ($(event.target).closest('.link-holder').length) return;
		$('.link-holder').removeClass('active');
		event.stopPropagation();
	});
	$('.table-general .col06 .link-holder .btn-status').not('.decline').click(function(){
		$(this).closest('.link-holder').hide();
		$(this).closest('.link-holder').next().removeClass('delete').addClass('normal').show();
		return false;
	});
	$('.table-general .col06 .link-holder .btn-status.decline').click(function(){
		$(this).closest('.link-holder').hide();
		$(this).closest('.link-holder').next().removeClass('normal').addClass('delete').show();
		return false;
	});
});
function popupbg(){
	if ($(window).height() < $("#wrapper").height()) {
		$(".popup-holder").css("height",$("#wrapper").height());
	} else {
		$(".popup-holder").css("height",$(window).height());
	}
}
function windowScroll(heightPopup){
	if ((($(window).height() - heightPopup)/2) > 0){
	wScroll = $(window).scrollTop() + (($(window).height() - heightPopup)/2);
	} else {
		wScroll = $(window).scrollTop() + 25;
	}
	if(($(".popup-holder").height()-wScroll-heightPopup) < 0){
		$(".popup-holder").height(wScroll+heightPopup + 20);
	}
}
jQuery.fn.fadeGallery = function(_options){
	var _options = jQuery.extend({
		slideElements:'ul.slide-list > li',
		pagerLinks:'ul.pager a',
		btnNext:'a.next',
		btnPrev:'a.prev',
		btnPlayPause:'a.play-pause',
		pausedClass:'paused',
		playClass:'playing',
		activeClass:'active',
		pauseOnHover:true,
		autoRotation:true,
		autoHeight:false,
		switchTime:3000,
		duration:650,
		event:'click'
	},_options);

	return this.each(function(){
		var _this = jQuery(this);
		var _slides = jQuery(_options.slideElements, _this);
		var _pagerLinks = jQuery(_options.pagerLinks, _this);
		var _btnPrev = jQuery(_options.btnPrev, _this);
		var _btnNext = jQuery(_options.btnNext, _this);
		var _btnPlayPause = jQuery(_options.btnPlayPause, _this);
		var _pauseOnHover = _options.pauseOnHover;
		var _autoRotation = _options.autoRotation;
		var _activeClass = _options.activeClass;
		var _pausedClass = _options.pausedClass;
		var _playClass = _options.playClass;
		var _autoHeight = _options.autoHeight;
		var _duration = _options.duration;
		var _switchTime = _options.switchTime;
		var _controlEvent = _options.event;

		var _hover = false;
		var _prevIndex = 0;
		var _currentIndex = 0;
		var _slideCount = _slides.length;
		var _timer;
		if(!_slideCount) return;
		_slides.hide().eq(_currentIndex).show();
		if(_autoRotation) _this.removeClass(_pausedClass).addClass(_playClass);
		else _this.removeClass(_playClass).addClass(_pausedClass);

		if(_btnPrev.length) {
			_btnPrev.bind(_controlEvent,function(){
				prevSlide();
				return false;
			});
		}
		if(_btnNext.length) {
			_btnNext.bind(_controlEvent,function(){
				nextSlide();
				return false;
			});
		}
		if(_pagerLinks.length) {
			_pagerLinks.each(function(_ind){
				jQuery(this).bind(_controlEvent,function(){
					if(_currentIndex != _ind) {
						_prevIndex = _currentIndex;
						_currentIndex = _ind;
						switchSlide();
					}
					return false;
				});
			});
		}

		if(_btnPlayPause.length) {
			_btnPlayPause.bind(_controlEvent,function(){
				if(_this.hasClass(_pausedClass)) {
					_this.removeClass(_pausedClass).addClass(_playClass);
					_autoRotation = true;
					autoSlide();
				} else {
					if(_timer) clearTimeout(_timer);
					_this.removeClass(_playClass).addClass(_pausedClass);
				}
				return false;
			});
		}

		function prevSlide() {
			_prevIndex = _currentIndex;
			if(_currentIndex > 0) _currentIndex--;
			else _currentIndex = _slideCount-1;
			switchSlide();
		}
		function nextSlide() {
			_prevIndex = _currentIndex;
			if(_currentIndex < _slideCount-1) _currentIndex++;
			else _currentIndex = 0;
			switchSlide();
		}
		function refreshStatus() {
			if(_pagerLinks.length) _pagerLinks.removeClass(_activeClass).eq(_currentIndex).addClass(_activeClass);
			_slides.eq(_prevIndex).removeClass(_activeClass);
			_slides.eq(_currentIndex).addClass(_activeClass);
		}
		function switchSlide() {
			_slides.eq(_prevIndex).fadeOut(_duration);
			_slides.eq(_currentIndex).fadeIn(_duration);
			refreshStatus();
			autoSlide();
		}

		function autoSlide() {
			if(!_autoRotation || _hover) return;
			if(_timer) clearTimeout(_timer);
			_timer = setTimeout(nextSlide,_switchTime+_duration);
		}
		if(_pauseOnHover) {
			_this.hover(function(){
				_hover = true;
				if(_timer) clearTimeout(_timer);
			},function(){
				_hover = false;
				autoSlide();
			});
		}
		refreshStatus();
		autoSlide();
	});
}