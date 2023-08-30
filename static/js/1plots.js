

$("#pag1_sub").click(function(){
	debugger;
	var res1="";
	var elements1 = document.getElementsByName("onclwk");
    for (var i = 0, l = elements1.length; i < l; i++)
    {
        if (elements1[i].checked)
        {
            res1+= elements1[i].value;
        }
    }
	var res4="";
	var elements4 = document.getElementsByName("clmoev");
    for (var i = 0, l = elements4.length; i < l; i++)
    {
        if (elements4[i].checked)
        {
            res4+= elements4[i].value;
        }
    }
	
	var res5="";
	var elements5 = document.getElementsByName("mnadcd");
    for (var i = 0, l = elements5.length; i < l; i++)
    {
        if (elements5[i].checked)
        {
            res5+= elements5[i].value;
        }
    }
	
	var res8="";
	var elements8 = document.getElementsByName("flgped");
    for (var i = 0, l = elements8.length; i < l; i++)
    {
        if (elements8[i].checked)
        {
            res8+= elements8[i].value;
        }
    }
	
	var res2="";
	var elements2 = document.getElementsByName("clotmo");
    for (var i = 0, l = elements2.length; i < l; i++)
    {
        if (elements2[i].checked)
        {
            res2+= elements2[i].value;
        }
    }

var res3="";
	var elements3 = document.getElementsByName("irdco");
    for (var i = 0, l = elements3.length; i < l; i++)
    {
        if (elements3[i].checked)
        {
            res3+= elements3[i].value;
        }
    }

	var res9="";
	var elements9 = document.getElementsByName("ecfmco");
    for (var i = 0, l = elements9.length; i < l; i++)
    {
        if (elements9[i].checked)
        {
            res9+= elements9[i].value;
        }
    }
	
	var res10="";
	var elements10 = document.getElementsByName("isrein");
    for (var i = 0, l = elements10.length; i < l; i++)
    {
        if (elements10[i].checked)
        {
            res10+= elements10[i].value;
        }
    }
	
	var res12="";
	var elements12 = document.getElementsByName("coreco");
    for (var i = 0, l = elements12.length; i < l; i++)
    {
        if (elements12[i].checked)
        {
            res12+= elements12[i].value;
        }
    }
	
	var res19="";
	var elements19 = document.getElementsByName("hywlon");
    for (var i = 0, l = elements19.length; i < l; i++)
    {
        if (elements19[i].checked)
        {
            res19+= elements19[i].value;
        }
    }
	
	var res21="";
	var elements21 = document.getElementsByName("afhpon");
    for (var i = 0, l = elements21.length; i < l; i++)
    {
        if (elements21[i].checked)
        {
            res21+= elements21[i].value;
        }
    }
	
	var res22="";
	var elements22 = document.getElementsByName("peimsc");
    for (var i = 0, l = elements22.length; i < l; i++)
    {
        if (elements22[i].checked)
        {
            res22+= elements22[i].value;
        }
    }
	
	var res23="";
	var elements23 = document.getElementsByName("stadol");
    for (var i = 0, l = elements23.length; i < l; i++)
    {
        if (elements23[i].checked)
        {
            res23+= elements23[i].value;
        }
    }
	
	var res31="";
	var elements31 = document.getElementsByName("oncoln");
    for (var i = 0, l = elements31.length; i < l; i++)
    {
        if (elements31[i].checked)
        {
            res31+= elements31[i].value;
        }
    }
	
	var res66="";
	var elements66 = document.getElementsByName("pmston");
    for (var i = 0, l = elements66.length; i < l; i++)
    {
        if (elements66[i].checked)
        {
            res66+= elements66[i].value;
        }
    }
	
	var res55="";
	var elements55 = document.getElementsByName("olprst");
    for (var i = 0, l = elements55.length; i < l; i++)
    {
        if (elements55[i].checked)
        {
            res55+= elements55[i].value;
        }
    }
	
	var algo="";
	var elements5a = document.getElementsByName("lastradio");
    for (var i = 0, l = elements5a.length; i < l; i++)
    {
        if (elements5a[i].checked)
        {
            algo+= elements5a[i].value;
        }
    }
	$.ajax({
            type: 'GET',
            url: '/page1data',
			
        contentType: 'application/json;charset=UTF-8',
            data: {
            'res1': res1,
            'res4': res4,
            'res5': res5,
            'res8': res8,
            'res2': res2,
			'res3':res3,
			'res9': res9,
            'res10': res10,
            'res12': res12,
			'res19':res19,
            'res21': res21,
            'res22': res22,
			'res23': res23,
			'res31':res31,
            'res66': res66,
            'res55': res55,
			'algo': algo
        },
            
        dataType:"json",
            success: function(data) {
				alert(data);
				//alerter();
				
			return false;
				//acheck();
              // window.location='register';
            },
        });
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









		
