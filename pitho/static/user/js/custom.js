jQuery(document).ready(function(){
	/** Load Data**/
	var abrt ="";
	var ajaxURL ="/get-item-list";
	jQuery(document).on("keyup",".ajax input[name='item_name']",function(){
		var textItem = jQuery(this).val();
		jQuery(".item_lists").html("").hide();
		if(textItem.length >2){
		  if(abrt){ abrt.abort();}
			abrt=jQuery.ajax({
				url:ajaxURL+"/"+textItem,
				success:function(data,textStatus,statusCode){
						jQuery(".item_lists").html("").hide();
						if (data.length > 0){
							jQuery(".item_lists").html(data).show();
						}
				},
				error:function(data,textStatus,statusCode){
				
				}
			});
		}
	})
	jQuery(document).on("click",".item_lists li",function(){
		jQuery(".ajax input[name='item_name']").val(jQuery(this).html());
		jQuery(".ajax input[name='item_price']").val(jQuery(this).data('id'));
		jQuery(".item_lists").html("").hide();
	});
	
});