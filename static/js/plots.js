

$("#butsave").click(function(){
	
		debugger;
		var unm=document.getElementById('email').value;
		var pswd=document.getElementById('password').value;
		if(unm=="admin@gmail.com" && pswd=="admin")
		{
			window.location.href ="home";
			return false;
		}
		else
		{
			alert("Check Entered Credentials");
			return false;
		}
});

	function alerter()
{
	debugger;
	alert('Data saved Successfully');
	window.location.href ="index";
}

function acheck(data)
{
	debugger;
				if(data=="Failure")
				{
					alert("Credentials not found");
					window.location.href ="patreg";
			return false;
				}
				if(data=="Success")
				{
					alert('Logged in Successfully');
				   window.location.href ="pathome";
			return false;
				}
}

function acheck1(data)
{
	debugger;
	if(data=="Failure")
				{
					alert(data);
					alert("Credentials not found");
					window.location.href ="docreg";
			return false;
				}
				if(data=="Success")
				{
					alert('Logged in Successfully');
				   window.location.href ="dochome";
			return false;
				}
}









		
