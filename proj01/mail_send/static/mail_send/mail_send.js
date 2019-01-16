// -----------------------------------------------------------------------
//	mail_send.js
//
//					Jan/16/2019
//
// -----------------------------------------------------------------------
jQuery (function ()
{
	jQuery("#outarea_aa").html ("*** mail_send.js *** start *** Jan/16/2019 ***")

	click_check_proc ()

	jQuery("#outarea_hh").html ("*** mail_send.js *** end *** Jan/16/2019 ***")
})

// -----------------------------------------------------------------------
function click_check_proc ()
{
	jQuery ("button.check").click (function ()
		{
		var str_out = "*** clicked ***<br />"

		jQuery("#" + this.id).css ("color","blue")

		jQuery("#outarea_bb").html(str_out)

		const url = "/mail_send/main/"

		var params = {}
		params['mail_to'] = jQuery("#mail_to").val()
		params['subject'] = jQuery("#subject").val()

		params['str_message'] = jQuery("#str_text").val()

		var str_out = ""
		str_out += params['mail_to'] + "<br />"
		str_out += params['subject'] + "<br />"
		str_out += params['str_message'] + "<br />"

		jQuery("#outarea_cc").html(str_out)

		jQuery.post(url,params,function ()
			{
			var str_tmp = "*** check *** ccc ***<br />"
			jQuery("#outarea_ee").html(str_tmp)
			})
		})
}

// -----------------------------------------------------------------------
