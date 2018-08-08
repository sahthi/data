$(document).ready(function(e){
	//alert("hello");
	$(function () { // on load of page
    // on a click on any link in the UL
    $("div.subnavbar>ul>li>a").on("click", function (e) { 
        e.preventDefault(); // cancel click
        // remove all active from all elements under UL
        $(this).closest("ul").find(".active").removeClass("active"); 
        // add active to the clicked
        $(this).addClass("active");
        // add active to the clicked's parent LI 
        $(this).parent().addClass("active");
        // hide all target divs
        $(".toggleDiv").hide();
        // show the one with ID= contents of data-target of clicked link
        $("#"+$(this).data("target")).show();
    }).first().click(); // click the first on load
});
	
	$('body').delegate("#create_repo",'click',function(evnt){
		

		$.ajax({
			url:'/createRepository/',
			type:'POST',
			data:{},
			success:function(response){
				result =JSON.parse(response);
				if (result.status && result.status==1){
				$('#mainData').html(result.html_data);
			}
			else{
				window.location.href=result.html_data;
			}
			},
			error:function(response){
				alert("Error");
			},
		});
		evnt.preventDefault();
	});

	$('body').delegate("#home_page",'click',function(evnt){
		$.ajax({
			url:'/',
			type:'POST',
			data:{},
			success:function(response){
				window.location.href="/";
			},
			error:function(response){
				alert("Error");
			},
		});
		evnt.preventDefault();
	});

	$('body').delegate("#delete_repo",'click',function(evnt){

		var rep_id = $('.radio').find('input[type="radio"]:checked').val();

		if (rep_id){
			//alert(rep_id);
		var dic={};
		dic["repo_id"]=rep_id;
		var a=confirm('are you sure?\nDo you really want to delete this record??');
        if (a == true){
        	
		$.ajax({
			url:'/deleteRepository/',
			type:'POST',
			data:dic,
			success:function(response){
				//alert(response);
				window.location.href="/";
			},
			error:function(response){
				//alert("error");
				window.location.href="/";

			},
		});
	}
}
		evnt.preventDefault();
	});

	$('body').delegate("#modify_repo",'click',function(evnt){
			
		
		var rep_id = $('.radio').find('input[type="radio"]:checked').val();
		
		if (rep_id){
			//alert(rep_id);
		var dic={};
		dic["repo_id"]=rep_id;
		
        	
		$.ajax({
			url:'/modifyRepository/',
			type:'POST',
			data:dic,
			success:function(response){
				//alert(response);
				result =JSON.parse(response);
				if (result.status && result.status==1){
				$('#mainData').html(result.html_data);
			}
			else{
				window.location.href=result.html_data;
			}
			},
			error:function(response){
				alert("Error");
			},
			
		});
	
}
		evnt.preventDefault();
	});

	$('body').delegate("#view_repo",'click',function(evnt){
		//alert("hello");
		var rep_id = $('.radio').find('input[type="radio"]:checked').val();
		//alert(rep_id);
		if (rep_id){
		var dic={};
		dic["repo_id"]=rep_id;
		$.ajax({
			url:'/viewRepository/',
			type:'POST',
			data:dic,
			success:function(response){

				result =JSON.parse(response);
				if (result.status && result.status==1){
				$('#homeData').html(result.html_data);
			}
			else{
				window.location.href=result.html_data;
			}
			},
			error:function(response){
				alert("Error");
			},
		});
	}
		evnt.preventDefault();
	});
	


	$('body').delegate("#new_repository",'submit',function(evnt){
		//alert($("#mysource").val());
			//console.log($("#mysource").val());
		if($("#repository_name").val() == ''){
			$("#repository_name_error").html("Enter Repository_name");

		}
		else if($("#mysource").val() == ''){
			$("#repository_name_error").html("");
			$("#myfile_error").html("Please upload file");

		}
		else{
			var data = new FormData($('#new_repository')[0]);

			$.ajax({
				url:"/addRepository/",
				data:data,
				type:"POST",
				processData: false,
    			contentType: false,
				success:function(response){
					//alert(response);
					result = JSON.parse(response);
					if (result.status == 0){
					$("#myfile_error").html(result.html_data);
					}
					else if (result.status == 2){
					$("#myreadme_error").html(result.html_data);
					}
					else{
						//alert(result.html_data);
						window.location.href = "/";
					}
				},
				error:function(response){
					alert("Internal Server Error,Please Try After Sometime");
				},

			});	
		}
		
		

		evnt.preventDefault();
	});

	

	$('body').delegate("#repo_execute",'click',function(evnt){
		
		$.ajax({
			url:'/executeRepository/',
			type:'POST',
			data:{},
			success:function(response){
				//alert(response);
				result =JSON.parse(response);
				if (result.status && result.status==1){
				$('#mainData').html(result.html_data);
			}
			else{
				window.location.href=result.html_data;
			}
			},
			error:function(response){
				alert("Error");
			},
		});

		evnt.preventDefault();
	});
	$('body').delegate("#repo_view",'click',function(evnt){
		
			var repo_id = $(this).data("id");
			var dic={};
			dic["repo_id"]=repo_id;
		$.ajax({
			url:'/viewRepository/',
			type:'POST',
			data:dic,
			success:function(response){
				result =JSON.parse(response);
				if (result.status && result.status==1){
				$('#homeData').html(result.html_data);
			}
			else{
				window.location.href=result.html_data;
			}
			},
			error:function(response){
				alert("Error");
			},
		});


		evnt.preventDefault();
	});



$('body').delegate("#script_execute","click",function(evnt){
	alert("running");
	check_array = new Array();
	$("input:checkbox.script_checkbox:checked").each(function(){
    //var sThisVal = (this.checked ? $(this).val() : "");
    //alert($(this).val());
    check_array.push($(this).val());
	});
	//alert(check_array);
	console.log(check_array);
	var iterations = $("#run_iterations").val();
    console.log(iterations);

   $.ajax({
    	url:"/runPlanExecution/",//"/runScriptExecution/",
    	type:"POST",
    	data:{"module_array":JSON.stringify(check_array),"module_iterations":iterations},
    	success:function(response){
    		alert(response);
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});


$('body').delegate("#repo_results","click",function(evnt){
	

    $.ajax({
    	url:"/resultRepository/",
    	type:"POST",
    	data:{},
    	success:function(response){
    		
    		result  = JSON.parse(response);
    		if (result.status && result.status == 1){
    			
    			$("#mainData").html(result.html_data);
    		}
    		else{
    			window.location.href=result.html_data;
    		}
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate("#repo_reports","click",function(evnt){
	//alert("hello")	;

    $.ajax({
    	url:"/reportsRepository/",
    	type:"POST",
    	data:{},
    	success:function(response){
    		
    		result  = JSON.parse(response);
    		if (result.status && result.status == 1){
    			
    			$("#mainData").html(result.html_data);
    		}
    		else{
    			window.location.href=result.html_data;
    		}
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".repo_analytics","click",function(evnt){
	//alert("hi");
	var ide = $(this).data("id");
	//alert(ide);

    $.ajax({
    	url:"/reportsRepository/",
    	type:"POST",
    	data:{"file_ide":ide},
    	success:function(response){
    		$("#mainData").html(response);
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".module_analytics","click",function(evnt){
	//alert("hi");
	var ide = $(this).data("id");
	//alert(ide);

    $.ajax({
    	url:"/reportsModuleRepository/",
    	type:"POST",
    	data:{"file_ide":ide},
    	success:function(response){
    		$("#mainData").html(response);
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});


$('body').delegate("#repo_monitor_execute","click",function(evnt){
	//alert("hi");
	//alert("hi")
    $.ajax({
    	url:"/monitorExecution/",
    	type:"POST",
    	data:{},

    	success:function(response){
			result =JSON.parse(response);
			//alert(result);
			if (result.status==1){
				$('#mainData').html(result.html_data);

			}
			else{
				window.location.href=result.html_data;
			}
			},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate("#clear_records","click",function(evnt){
	//alert("hi");
	//alert("hi")
    $.ajax({
    	url:"/clearRecords/",
    	type:"POST",
    	data:{},
    	success:function(response){
				result =JSON.parse(response);
				if (result.status==1){
				$('#mainData').html(result.html_data);
			
			}
			else if (result.status && result.status == 2){
				alert(result.html_data);
			}
		else{
				window.location.href=result.html_data;
			}
			},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".script_result","click",function(evnt){
	//alert("hi");
	evnt.preventDefault();
	var file_id = $(this).data("value");
	//alert(file_id);
   	$.ajax({
    	url:"/monitorScriptLogs/",
    	type:"POST",
    	data:{"file_id":file_id},
    	success:function(response){
    		//$("#mainData").html(response);
    		$("#show_script_result").html(response);
    		$('#myModal').modal('show');
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".view_logs","click",function(evnt){
	//alert("hi");
	evnt.preventDefault();
	var file_id = $(this).data("value");
	//alert(file_id);
   	$.ajax({
    	url:"/showScriptLog/",
    	type:"POST",
    	data:{"file_id":file_id},
    	success:function(response){
    		//$("#mainData").html(response);
    		$("#show_script_result").html(response);
    		$('#myModal').modal('show');
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".predict_class","click",function(evnt){
	//alert("hi");
	evnt.preventDefault();
	var file_id = $(this).data("value");
	//alert(file_id);
   	$.ajax({
    	url:"/showPredictions/",
    	type:"POST",
    	data:{"file_id":file_id},
    	success:function(response){
    		
    		$("#show_script_result").html(response);
    		$('#myModal').modal('show');
    	},
    	error:function(response){
    		alert("Error");
    	},
    });
	evnt.preventDefault();
});

$('body').delegate(".delete_script","click",function(evnt){
	var file_id = $(this).data("value");
	//alert(file_id);
	
	var a=confirm('are you sure?\nDo you really want to delete this record??');
	if (a == true){
		$(this).hide();

	$.ajax({
		url:"/deleteScript/",
    	type:"POST",
    	data:{"file_id":file_id},
    	success:function(response){
    		result = JSON.parse(response);
    		if (result.status && result.status == 1 ){
    			//alert("deleted");
    			
    		}
    		else{
    			alert("Try again");
    		}
    	},
    	error:function(response){
    		alert("Error");
    	},

	});
}
	evnt.preventDefault();
});

//module_modify_upload

$('body').delegate("#module_modify_upload",'submit',function(evnt){

		if($("#mymodifyfile").val() == ''){
			
			$("#mymodify_error").html("Please upload file");
		}
		else{
			var data = new FormData($('#module_modify_upload')[0]);

			$.ajax({
				url:"/modifyModuleUpload/",
				data:data,
				type:"POST",
				processData: false,
    			contentType: false,
				success:function(response){
					alert(response);
				},
				error:function(response){
					alert("Internal Server Error,Please Try After Sometime");
				},

			});			
		}
		
		

		evnt.preventDefault();
	});



	e.preventDefault();
});