	function doajax(degreee,edu){
		$.ajax({
			url: "/static",
			type: 'GET',
			dataType: 'json',
			data:{'edu':edu,'degreee':degreee},
			error:function() {
				alert("ajax加载失败！");
			}
		})
	}