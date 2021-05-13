/*jshint forin:true, noarg:true, noempty:true, eqeqeq:true, bitwise:true, strict:true, undef:true, unused:false, curly:true, browser:true, devel:true, jquery:true, es5:true, indent:4, maxerr:50 */
/*global impress */
(function($,undefined){
	'use strict';

	var ie = (navigator.appVersion.indexOf("MSIE") !== -1) ? parseFloat(navigator.appVersion.split("MSIE")[1]) : 99;

	$(function(){
		
		$('body').removeClass('preload');

		if(ie > 10) {
			try{
				var imprs = impress();
				imprs.init();
				document.addEventListener('impress:stepenter',function(e){
					var fn = e.target.id + 'PageAnimate';
					if(window[fn]){
						window[fn]();
					}
				});
			}catch(e){
				console.log(e);
			}
		}

		//Portfolio
		$("a.dwn-vcard").click(function(){
			return false;
		});

		$('#cat_01').click(function(){
			$('#portfolio-list').removeClass().addClass('cat_01');
		});
		$('#cat_02').click(function(){
			$('#portfolio-list').removeClass().addClass('cat_02');
		});
		$('#cat_03').click(function(){
			$('#portfolio-list').removeClass().addClass('cat_03');
		});
		$('#cat_04').click(function(){
			$('#portfolio-list').removeClass().addClass('cat_04');
		});
		$('#all1').click(function(){
			$('#portfolio-list').removeClass().addClass('all');
		});
		$('#cat_05').click(function(){
			$('#portfolio-list2').removeClass().addClass('cat_05');
		});
		$('#cat_06').click(function(){
			$('#portfolio-list2').removeClass().addClass('cat_06');
		});
		$('#cat_07').click(function(){
			$('#portfolio-list2').removeClass().addClass('cat_07');
		});
		$('#all2').click(function(){
			$('#portfolio-list2').removeClass().addClass('all');
		});

		// for Skill Graph Animate
		var graph_height = $('.graph-skill').height(),
			$graph_bars = $(".graph-skill li");
		
		$graph_bars.each(function(){
			var $this = $(this),
				$elm = $this.children("span.bar-title"),
				val = parseFloat($elm.text());

			val = (!val || val<1)  ? 1 :
				val>100 ? 100 : val;

			$this
				.css({
					'margin-top': graph_height*(100-val)/100,
					height: graph_height*val/100+'px'
				})
				.data('percentValue', val);

			$elm.html(val+"%");
		});

		// Custom page animations

		var resumePageAnimate = function(){
			var dly=1;
			$graph_bars.each(function(){
				var $this=$(this),
					val = $this.data('percentValue'),
					scl = 0.2;
				$this
					.delay(dly)
					.animate({
						'margin-top': graph_height*(100-(val*scl))/100,
						height: graph_height*val*scl/100+'px'
					},200,'swing')
					.animate({
						'margin-top': graph_height*(100-val)/100,
						height: graph_height*val/100+'px'
					},300, 'swing');
				dly+=120;
			});
		};

		
		// ColorBox
		$(".port_group").colorbox({
			rel:'port_group',
			transition:"fade",
			scrolling:false,
			returnFocus:false,
			maxHeight:window.innerHeight-50,
			maxWidth:window.innerWidth-50
		});


		// placeholders
		$('div.lblplaceholder input, div.lblplaceholder textarea').focus(function(){
			var id = $(this).attr('data-lbl');
			$('label#'+ id).css({
				'visibility':'hidden'
			});
		});
		$('div.lblplaceholder input, div.lblplaceholder textarea').blur(function(){
			if(!$(this).val()){
				var id = $(this).attr('data-lbl');
				$('label#'+ id).css({
					'visibility':'visible'
				});
			}
		});
		$('div.lblplaceholder label').click(function(){
			$('div.lblplaceholder label').css({'visibility':'visible'});
			$("div.lblplaceholder input[data-lbl='"+ $(this).attr('data-id') +"']").focus();
			$("div.lblplaceholder textarea[data-lbl='"+ $(this).attr('data-id') +"']").focus();
			$(this).css({
				'visibility':'hidden'
			});
		});

		// Portfolio li
		var ul_filter_li =
		$('section.portfolio_container ul.filter li').click(function(){
			ul_filter_li.removeClass('active');
			$(this).addClass('active');
		});


		// Skin Choose Panel
		$('div.skin-selector a#toggle-panel').click(function(){
			$('div.skin-selector').toggleClass('openpanel');
			return false;
		});
		var bodyClass = {
			backgrlound:false,
			forground:false,
			forecolor:false
		};
		$('div.pattern-bg ul li,div.color-bg ul li').click(function(){
			if(bodyClass.background){
				$('body').removeClass(bodyClass.background);
			}
			bodyClass.background = $(this).attr('class');
			$('body').addClass(bodyClass.background);
		});
		$('div.style-color ul li').click(function(){
			if(bodyClass.forground){
				$('body').removeClass(bodyClass.forground);
			}
			bodyClass.forground = 'fg-'+$(this).attr('class');
			$('body').addClass(bodyClass.forground);
		});
		$('div.font-color ul li').click(function(){
			if(bodyClass.forecolor){
				$('span.h1-text').removeClass(bodyClass.forecolor);
			}
			bodyClass.forecolor = 'fc-'+$(this).attr('class');
			$('span.h1-text').addClass(bodyClass.forecolor);
		});

		//IMG hover
		$('.dwn-vcard').mouseover(function(){
			$('.me').addClass('hover');
		}).mouseout(function(){
			$('.me').removeClass('hover');
		});

		// for Animate Main Menu

		$('nav.mainmenu ul > li').mouseover(function(){
			$(this).stop().animate({
				'right':'0px'
			},100);
		}).mouseout(function(){
			$(this).stop().animate({
				'right':'-140px'
			},400);
		});

		// Contact Form Validators
		var
		emailPattern = /^[a-z0-9+_%.\-]+@(?:[a-z0-9\-]+\.)+[a-z]{2,6}$/i,
		validateText = function (str,len){
			return str.length >= len;
		},
		validateEmail = function (str){
			return emailPattern.test(str);
		},
		updateAjax = function(){
			// Contact form
			$('#contact-form').submit(function(){
				var target=$('#name'), err = false;

				target = $('#name');
				if( validateText(target.val(),3) ){
					target.removeClass('err').addClass('ok');
				}else{
					target.removeClass('ok').addClass('err');
					err = true;
				}

				target = $('#mail');
				if( validateEmail(target.val()) ){
					target.removeClass('err').addClass('ok');
				}else{
					target.removeClass('ok').addClass('err');
					err = true;
				}

				target = $('#msg');
				if( validateText(target.val(),10) ){
					target.removeClass('err').addClass('ok');
				}else{
					target.removeClass('ok').addClass('err');
					err = true;
				}

				if(!err){
					$('#ifrm').animate({
						height:'70px'
					},700);
				}

				return !err;
			});
		};
		updateAjax();
	});

})(jQuery);