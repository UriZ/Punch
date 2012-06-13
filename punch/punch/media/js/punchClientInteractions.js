


function onRepunchClick(punchId)
{ 
	$.get("/users/1/collections", function(data)
	{
		
		var parsedData = jQuery.parseJSON(data);
		
		toggleRePunchDialogue(punchId,parsedData)

		
	});

}

function repunch(punchId, targetCollectionId)
{
	$.get("/repunch/"+punchId+"/"+targetCollectionId, function(data) {
			

		});
}



/**
 * open a punch when clicking on the image 
 */
function togglePunch(id)
{
	
	var visible = toggleOverlay();
	if (visible)
	{
			var punch = $(document.getElementById(id))
			var src = punch.find("img").attr("imageSource")
			zoomPunch(1,src)

	}
}


	



function toggleOverlay()
{
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
	el = document.getElementById("overlayWrapper");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
	return (el.style.visibility == "visible");
}

function toggleRePunchDialogue(id,data)
{
	
	if (toggleOverlay())
	{
		
		/**
		 * build the combobox 
		 */
		debugger;
		var div = document.createElement('div');
		$(div).attr("class","ui-widget");
		
		var select = document.createElement('select');
		$(select).attr("id","combobox");
		$(select).attr("targetPunchId",id);
		

		
		jQuery.each(data,function()
		{
			var option = document.createElement('option');
			$(option).attr("value",this.id);
			$(option).html(this.title)
			$(select).append($(option));
		}
		
			);	
		
			$(div).append($(select));
		
		
		$("#overlayContent").bind('click', function (event) {
			  event.stopPropagation();

		});
		
		var repunchWidget = document.createElement('div');
		$(repunchWidget).attr("class","repunchWidget");
		$(repunchWidget).append($(div));
		
		$("#overlayContent").empty()
		$("#overlayContent").append($(repunchWidget))
		openCombo()
	
	}
}



