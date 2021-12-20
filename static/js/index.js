const Koffing = window.Koffing;

function updateMon(num, id = -1, _callback = null) {
	var match = false;
	if (id == -1) {
		//id = $(".species_dropdown[id="+parseInt(num)+"] option:selected").attr("value");
		name = $(".species_dropdown[id="+num+"]").val();
		matches = $("#species_"+num+" option").filter(function() {
           return ($(this).val().toLowerCase() === name.toLowerCase());
		});
		if (matches.length == 1)
		{
			match = true;
			id = matches.data("id");
			$(".species_dropdown[id="+num+"]").data("id", matches.data("id")).data("name", name);
		}
	}
	else { match = true; }
	if (match)
	{
		$.ajax(
		{
			type:"GET",
			url: "/viz/updatemon",
			data: {
				mon_id: id
			},
			//async: false,
			success: function( pack ) 
			{
				var data;
				data = pack.split("#");
				var id_string;
				id_string = data[1];
				mon_team_id = data[4];
				e_pfx = "#"+parseInt(mon_team_id)+" "
				//if (data.species_form_name != "")
				//{
				//	id_string += "-" + data.species_form_name.toLowerCase().split("-").join("");
				//}
				console.log(data[0]);
				mon_lvl = $(e_pfx+".level_input").val();
				$(e_pfx+".mon_name").text(data[0]);
				$(e_pfx+".gendersprite").css("left", String($(e_pfx+".mon_name").width()+14)+"px");
				$(e_pfx+".lvl").text(" Lv. "+String(mon_lvl))
				// GENDERS
				$(e_pfx+".gender_dropdown option").remove();
				ratio = data[8];
				if (ratio != 8 && ratio != -1) // male
				{
					$(e_pfx+".gender_dropdown").append($('<option>', {
						value: "M"+"#"+parseInt(mon_team_id),
						text: "Male",
					}));
				}
				$(e_pfx+".gendersprite").attr("src", "../static/img/gender/m.png");
				if (ratio != 0 && ratio != -1) // female
				{
					$(e_pfx+".gender_dropdown").append($('<option>', {
						value: "F"+"#"+parseInt(mon_team_id),
						text: "Female",
					}));
				}
				if (ratio == 8) { $(e_pfx+".gendersprite").attr("src", "../static/img/gender/f.png"); }
				if (ratio == -1) // genderless
				{
					$(e_pfx+".gender_dropdown").append($('<option>', {
						value: "X"+"#"+parseInt(mon_team_id),
						text: "Genderless",
					}));
				}
				gender = $(".gender_dropdown[id="+parseInt(num)+"] option:selected").attr("value").slice(0,1);
				if (gender == "X")
				{
					$(e_pfx+".gendersprite").css("display", "none");
					$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18)+"px");
				}
				else
				{
					$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18+36)+"px");
					$(e_pfx+".gendersprite").css("display", "inline");
				}
				console.log(String($(e_pfx+".mon_name").width())+"px");
				$(e_pfx+".mon_id_string").text(data[1]);
				$(e_pfx+".monsprite").attr("src", "../static/img/species/"+id_string+".png");
				// TYPES
				$(e_pfx+".type1").attr("src", "../static/img/typebars/"+String(data[2])+".png");
				if (parseInt(data[3]) != -1)
				{
					$(e_pfx+".type2").attr("src", "../static/img/typebars/"+String(data[3])+".png");
					$(e_pfx+".type2").css("visibility", "visible/inherit");
				}
				else
				{
					$(e_pfx+".type2").css("visibility", "hidden");
				}
				// ABILITIES
				$(e_pfx+".ability_dropdown option").remove();
				$(e_pfx+".ability_dropdown").append($('<option>', {
					value: data[5]+"#"+parseInt(mon_team_id),
					text: data[5],
				}));
				$(e_pfx+".ability_name").text(data[5]);
				if (data[6]) {
					$(e_pfx+".ability_dropdown").append($('<option>', {
						value: data[6]+"#"+parseInt(mon_team_id),
						text: data[6]
					}));
				}
				if (data[7]) {
					$(e_pfx+".ability_dropdown").append($('<option>', {
						value: data[7]+"#"+parseInt(mon_team_id),
						text: data[7]
					}));
				}
				if (_callback) { _callback(); }
			}
		});
	}
	return false;
}

function updateItem(num) {
	var id;
	id = $(".item_dropdown[id="+parseInt(num)+"] option:selected").attr("value");
	$.ajax(
    {
        type:"GET",
        url: "/viz/updateitem",
        data: {
			item_id: id
		},
        success: function( pack ) 
        {
			var data;
			data = pack.split("#");
			mon_team_id = data[2];
			e_pfx = "#"+parseInt(mon_team_id)+" "
			if (data[1] != -1)
			{
				$(e_pfx+".itemsprite").attr("src", "../static/img/items/"+String(data[1])+".png");
				$(e_pfx+".itemsprite").css("display", "inline");
				$(e_pfx+".item_name").text(data[0]);
				$(e_pfx+".item_name").css("display", "inline");
			}
			else
			{
				$(e_pfx+".itemsprite").css("display", "none");
				$(e_pfx+".item_name").css("display", "none");
			}
		}
	});
	return false;
}

function updateLevel(num) {
	e_pfx = "#"+String(num)+" ";
	mon_lvl = $(e_pfx+".level_input").val();
	if (mon_lvl <= 100 && mon_lvl >= 1)
	{
	//lvidx = $(e_pfx+".mon_name").text().indexOf(" Lv.");
	//if (lvidx == -1) { lvidx = $(e_pfx+".mon_name").text().length; }
	//newtext = $(e_pfx+".mon_name").text().slice(0, lvidx)+" Lv. "+String(mon_lvl);
		$(e_pfx+".lvl").text(" Lv. "+String(mon_lvl));
	}
	if (mon_lvl > 100) { $(e_pfx+".level_input").val(100); }
	else if (mon_lvl < 1) { $(e_pfx+".level_input").val(1); }
	return false;
}

function updateAbility(num) {
	e_pfx = "#"+String(num)+" ";
	var name;
	name = $(".ability_dropdown[id="+parseInt(num)+"] option:selected").text();
	$(e_pfx+".ability_name").text(name);
	return false;
}

function updateGender(num) {
	e_pfx = "#"+String(num)+" ";
	var gender;
	gender = $(".gender_dropdown[id="+parseInt(num)+"] option:selected").attr("value").slice(0,1);
	if (gender == "X")
	{
		$(e_pfx+".gendersprite").css("display", "none");
		$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18)+"px");
	}
	else
	{
		$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18+36)+"px");
		$(e_pfx+".gendersprite").attr("src", "../static/img/gender/"+gender.toLowerCase()+".png");
		$(e_pfx+".gendersprite").css("display", "inline");
	}
	return false;
}

function updateMove(slot, num, selector=null, id = -2) {
	selector = $(".move_dropdown_"+String(slot)+"[id="+String(num)+"]");
	e_pfx = "#"+String(num)+" ";
	if (id == -2)
	{
		id = $(".move_dropdown_"+parseInt(slot)+"[id="+parseInt(num)+"] option:selected").attr("value");
	}
	$.ajax(
    {
        type:"GET",
        url: "/viz/updatemove",
        data: {
			move_id: id
		},
        success: function( pack ) 
        {
			var data;
			data = pack.split("#");
			mon_team_id = data[3];
			e_pfx = "#"+parseInt(mon_team_id)+" ";
			var hidecheck;
			hidecheck = false;
			move_id = id.split("#")[0];
			if (data[0]) // new move chosen
			{
				for (i = 1; i <= 4; i++) // move lockouts
				{
					if (data[0] && i != slot) // disabling moves on others, if no move
					{
						//console.log("disabling "+move_id+"#"+String(i)+"#"+data[3]+" on slot "+String(i));
						$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"] option[value='"+move_id+"#"+String(i)+"#"+data[3]+"']").attr("disabled", "disabled");

					}
					if (selector.data("prev_move").split("#")[0] != -1) // enabling previous move on others, if it was a move
					{
						//console.log("enabling "+selector.data("prev_move")+" on slot "+String(i));
						$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"] option[value='"+selector.data("prev_move").split("#")[0]+"#"+String(i)+"#"+data[3]+"']").removeAttr("disabled");
					}
				}
				
				for (i = data[2]; i <= 4; i++)
				{
					
					if ($(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"] option:selected").attr("value").split("#")[0] != -1 && !hidecheck) // move selected
					{
						//$(e_pfx+".move_"+String(i)).css("visibility", "visible/inherit");
						$(e_pfx+".move_"+String(i)).css("display", "inline");
						
						$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").removeAttr("disabled");
					}
					else // move not selected
					{
						//$(e_pfx+".move_"+String(i)).css("visibility", "hidden");
						$(e_pfx+".move_"+String(i)).css("display", "none");
						if (hidecheck)
						{
							// (i) is a later moveslot
							$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").data("prev_move", $(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").val()).attr("disabled", "disabled").val("-1#"+String(i)+"#"+data[3]);
							if ($(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").data("prev_move").split("#")[0] != -1) // enabling previous move on others, if it was a move
							{
								for (j = 1; j <= 4; j++)
								{
									$(".move_dropdown_"+String(j)+"[id="+parseInt(data[3])+"] option[value='"+
										$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").data("prev_move").split("#")[0]+
										"#"+String(j)+"#"+data[3]+"']").removeAttr("disabled");
								}
							}
						}
						else
						{
							$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").removeAttr("disabled");
						}
						hidecheck = true;
					}
				}
				$(e_pfx+".move_name_"+parseInt(data[2])).text(data[0]);
				$(e_pfx+".movesprite_"+parseInt(data[2])).attr("src", "../static/img/typeicons/"+parseInt(data[1])+".png");
			}
			else // no move chosen
			{
				for (j = 1; j <= 4; j++)
				{
					$(".move_dropdown_"+String(j)+"[id="+parseInt(data[3])+"] option[value='"+
						$(".move_dropdown_"+data[2]+"[id="+parseInt(data[3])+"]").data("prev_move").split("#")[0]+
						"#"+String(j)+"#"+data[3]+"']").removeAttr("disabled");
				}
				for (i = parseInt(data[2]); i <= 4; i++)
				{
					//$(e_pfx+".move_"+String(i)).css("visibility", "hidden");
					$(e_pfx+".move_"+String(i)).css("display", "none");
					if (i > data[2])
					{
						$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").data("prev_move", $(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").val()).attr("disabled", "disabled").val("-1#"+String(i)+"#"+data[3]);
						for (j = 1; j <= 4; j++) // recursive enable
						{
							console.log(".move_dropdown_"+data[2]+"[id="+parseInt(data[3])+"]");
							$(".move_dropdown_"+String(j)+"[id="+parseInt(data[3])+"] option[value='"+
								$(".move_dropdown_"+String(i)+"[id="+parseInt(data[3])+"]").data("prev_move").split("#")[0]+
								"#"+String(j)+"#"+data[3]+"']").removeAttr("disabled");
						}
					}
				}
			}
			selector.data("prev_move", id);
		}
	});
	return false;
}

function updateMoveset(num, id = -1) {
	e_pfx = "#"+String(num)+" ";
	var match = false;
	if (id == -1) {
		//id = $(".species_dropdown[id="+parseInt(num)+"] option:selected").attr("value");
		name = $(".species_dropdown[id="+num+"]").val();
		matches = $("#species_"+num+" option").filter(function() {
           return ($(this).val().toLowerCase() === name.toLowerCase());
		});
		if (matches.length == 1)
		{
			match = true;
			id = matches.data("id");
		}
	}
	else { match = true; }
	if (match)
	{
	//if (id == -1) {
	//	id = $(".species_dropdown[id="+parseInt(num)+"] option:selected").attr("value");
	//}
		$.ajax(
		{
			type:"GET",
			url: "/viz/updatemoveset",
			data: {
				mon_id: id
			},
			success: function( pack ) 
			{
				var data;
				data = pack.split("#");
				mon_team_id = data[0];
				e_pfx = "#"+parseInt(mon_team_id)+" ";
				slot = 1;
				for (slot = 1; slot <= 4; slot++)
				{
					dropdown = $(e_pfx+".move_dropdown_"+parseInt(slot)+"[id="+parseInt(num)+"]");
					$(e_pfx+".move_dropdown_"+parseInt(slot)+"[id="+parseInt(num)+"] option").remove();
					if (slot != 1)
					{
						dropdown.append($('<option>', {
								value: String(-1)+"#"+parseInt(slot)+"#"+parseInt(mon_team_id),
								text: "(no move)",
							}));
					}
					for (i = 0; i < (data.length-1)/2; i++)
					{
						dropdown.append($('<option>', {
							value: parseInt(data[(2*i)+1+1])+"#"+parseInt(slot)+"#"+parseInt(mon_team_id),
							text: data[(2*i)+1],
						}));
					}
				}
				//$(e_pfx+".move_name_1").text(data[1]);
				//$(e_pfx+".movesprite_1").attr("src", "../static/img/typeicons/"+parseInt(data[2])+".png");
				updateMove(1, num);
			}
		});
	}
}

function makeImage() {
	var name = "Anonymous";
	if ($(".trainer_name").val()) { name = $(".trainer_name").val(); }
	var teamname = "Untitled Team";
	if ($(".team_name").val()) { teamname = $(".team_name").val(); }
	$.ajax(
	{
		type: "GET",
		url: "/viz/makeimage",
		data: {
			//species_id_1: $("#1 .species_dropdown[id=1] option:selected").attr("value"),
			species_id_1: $("#1 .species_dropdown[id=1]").data("id"),
			name_width_1: $("#1 .mon_name").width(),
			gender_1: $("#1 .gender_dropdown[id=1] option:selected").attr("value").slice(0,1),
			level_1: $("#1 .level_input").val(),
			item_1: $("#1 .item_dropdown[id=1] option:selected").attr("value"),
			ability_1: $("#1 .ability_dropdown[id=1] option:selected").attr("value"),
			move_1_1: $("#1 .move_dropdown_1[id=1] option:selected").attr("value"),
			move_2_1: $("#1 .move_dropdown_2[id=1] option:selected").attr("value"),
			move_3_1: $("#1 .move_dropdown_3[id=1] option:selected").attr("value"),
			move_4_1: $("#1 .move_dropdown_4[id=1] option:selected").attr("value"),
			
			species_id_2: $("#2 .species_dropdown[id=2]").data("id"),
			name_width_2: $("#2 .mon_name").width(),
			gender_2: $("#2 .gender_dropdown[id=2] option:selected").attr("value").slice(0,1),
			level_2: $("#2 .level_input").val(),
			item_2: $("#2 .item_dropdown[id=2] option:selected").attr("value"),
			ability_2: $("#2 .ability_dropdown[id=2] option:selected").attr("value"),
			move_1_2: $("#2 .move_dropdown_1[id=2] option:selected").attr("value"),
			move_2_2: $("#2 .move_dropdown_2[id=2] option:selected").attr("value"),
			move_3_2: $("#2 .move_dropdown_3[id=2] option:selected").attr("value"),
			move_4_2: $("#2 .move_dropdown_4[id=2] option:selected").attr("value"),
			
			species_id_3: $("#3 .species_dropdown[id=3]").data("id"),
			name_width_3: $("#3 .mon_name").width(),
			gender_3: $("#3 .gender_dropdown[id=3] option:selected").attr("value").slice(0,1),
			level_3: $("#3 .level_input").val(),
			item_3: $("#3 .item_dropdown[id=3] option:selected").attr("value"),
			ability_3: $("#3 .ability_dropdown[id=3] option:selected").attr("value"),
			move_1_3: $("#3 .move_dropdown_1[id=3] option:selected").attr("value"),
			move_2_3: $("#3 .move_dropdown_2[id=3] option:selected").attr("value"),
			move_3_3: $("#3 .move_dropdown_3[id=3] option:selected").attr("value"),
			move_4_3: $("#3 .move_dropdown_4[id=3] option:selected").attr("value"),
			
			species_id_4: $("#4 .species_dropdown[id=4]").data("id"),
			name_width_4: $("#4 .mon_name").width(),
			gender_4: $("#4 .gender_dropdown[id=4] option:selected").attr("value").slice(0,1),
			level_4: $("#4 .level_input").val(),
			item_4: $("#4 .item_dropdown[id=4] option:selected").attr("value"),
			ability_4: $("#4 .ability_dropdown[id=4] option:selected").attr("value"),
			move_1_4: $("#4 .move_dropdown_1[id=4] option:selected").attr("value"),
			move_2_4: $("#4 .move_dropdown_2[id=4] option:selected").attr("value"),
			move_3_4: $("#4 .move_dropdown_3[id=4] option:selected").attr("value"),
			move_4_4: $("#4 .move_dropdown_4[id=4] option:selected").attr("value"),
			
			species_id_5: $("#5 .species_dropdown[id=5]").data("id"),
			name_width_5: $("#5 .mon_name").width(),
			gender_5: $("#5 .gender_dropdown[id=5] option:selected").attr("value").slice(0,1),
			level_5: $("#5 .level_input").val(),
			item_5: $("#5 .item_dropdown[id=5] option:selected").attr("value"),
			ability_5: $("#5 .ability_dropdown[id=5] option:selected").attr("value"),
			move_1_5: $("#5 .move_dropdown_1[id=5] option:selected").attr("value"),
			move_2_5: $("#5 .move_dropdown_2[id=5] option:selected").attr("value"),
			move_3_5: $("#5 .move_dropdown_3[id=5] option:selected").attr("value"),
			move_4_5: $("#5 .move_dropdown_4[id=5] option:selected").attr("value"),
			
			species_id_6: $("#6 .species_dropdown[id=6]").data("id"),
			name_width_6: $("#6 .mon_name").width(),
			gender_6: $("#6 .gender_dropdown[id=6] option:selected").attr("value").slice(0,1),
			level_6: $("#6 .level_input").val(),
			item_6: $("#6 .item_dropdown[id=6] option:selected").attr("value"),
			ability_6: $("#6 .ability_dropdown[id=6] option:selected").attr("value"),
			move_1_6: $("#6 .move_dropdown_1[id=6] option:selected").attr("value"),
			move_2_6: $("#6 .move_dropdown_2[id=6] option:selected").attr("value"),
			move_3_6: $("#6 .move_dropdown_3[id=6] option:selected").attr("value"),
			move_4_6: $("#6 .move_dropdown_4[id=6] option:selected").attr("value"),
			
			avatar: $(".avatar_dropdown option:selected").val(),
			name: name,
			teamname: teamname,
			game: $(".game option:selected").val(),
			team_size: team_size,
		},
		success: function(img)
		{
			//img_disp = $("body").append($('<img>', {
			//	src: "data:image/png;base64,"+img,
			//	style: "width: 75vw;"
			//}));
			//let parsedTeam = window.Koffing.parse(teamCode);

			// This will log a PokémonTeamSet object:
			//console.log(parsedTeam);
			
			$(".output_img").on("load", function() {
				$(".image_overlay").css("visibility", "visible").css("backdrop-filter", "blur(2px)");
			}).attr("src", "data:image/png;base64,"+img);
			$(".save_as").attr("href", "data:image/png;base64,"+img).attr("download", teamname+".png");
		}
	});
}

function parseTeam() {
	input = $(".import_text").val();
	if (input.length < 1) { return false; }
	parsedTeam = window.Koffing.parse(input);
	//console.log(parsedTeam);
	mons = parsedTeam["teams"][0]["pokemon"];
	imported_name = parsedTeam["teams"][0]["name"];
	if (!$(".team_name").val())
	{
		$(".team_name").val(imported_name.slice(0, $(".team_name").attr("maxlength")));
		if (parsedTeam["teams"][0]["name"] == "Untitled")
		{
			$(".team_name").val("Untitled Team");
		}
	}
	console.log(mons);
	if (team_size != mons.length) {
		while (team_size < mons.length) { addSlot(); }
		while (team_size > mons.length) { removeSlot(); }
	}
	var genders = [];
	for (var mon of mons)
	{
		if (mon["gender"])
		{
			genders.push(mon["gender"]);
		}
		else
		{
			genders.push("X");
		}
	}
	console.log(genders);
	//if (mons.length < 6)
	//{
		var slot_text = " ";
		var import_text = "Only "+mons.length;
		//if (mons.length == 0) { import_text = "No"; }
		//if (mons.length != 5) { slot_text = "s "+String(mons.length+1)+" to "; }
		$("#teamsize").text(mons.length+" Pokemon imported").css("border", "2px solid #000").css("background-color", "#fff");
	//}
	//else
	//{
	//	$("#teamsize").text("").css("border", "0px");
	//}
	var mon_counter;
	no_move_text = "";
	no_ability_text = "";
	var invalid_species_text = "";
	$(".warn_box[id=invalidspecies]").remove();
	$(".warn_box[id=invaliditem]").remove();
	$(".warn_box[id=invalidmove]").remove();
	$(".warn_box[id=invalidability]").remove();
	//$("form").not(".ui, .import_box").trigger("reset");
	for (var mon of mons)
	{
		var mon_item;
		if (!mon["item"]) { mon_item = "-1"; }
		else { mon_item = mon["item"]; }
		moves = ["", "", "", ""];
		for (i = 0; i < 4; i++)
		{
			if (mon["moves"].length > i)
			{
				moves[i] = mon["moves"][i];
				if (moves[i].includes("["))
				{
					moves[i] = moves[i].slice(0, moves[i].indexOf("[")-1);
				}
			}
		}
		mon_counter = mons.indexOf(mon)+1;
		if (mon["moves"].length < 1)
		{
			no_move_text += String(mon_counter)+", ";
		}
		if (!mon["ability"])
		{
			no_ability_text += String(mon_counter)+", ";
		}
		import_ability = mon["ability"];
		if (!import_ability) { import_ability = ""; }
		$.ajax(
		{
			type: "GET",
			url: "/viz/monlookup",
			//async: false,
			data: {
				mon_name: mon["name"],
				mon_item: mon_item,
				move_1: moves[0],
				move_2: moves[1],
				move_3: moves[2],
				move_4: moves[3],
				mon_counter: mon_counter,
				mon_ability: import_ability,
				mon_level: mon["level"],
			},
			success: function(pack)
			{
				if (pack.split("#")[0] == 'invalid species')
				{
					$("#nomoves").before($('<div>', {
						class: "warn_box",
						id: "invalidspecies",
						style: "background-color: #ff8329; line-height: 26px; border: 2px solid #341b08",
						text: "Invalid species name: '"+pack.split("#")[2]+"'",
					}));
					
				}
				else
				{
					values = pack.split("#");
					// DISPLAY NAME | ID STRING (sprite) | TYPE 1 | TYPE 2 | NUM | ABILITY 1 | ABILITY 2 | ABILITY 3 | GENDER RATIO | ITEM ID | M1 NAME | M1 TYPE | M2 NAME | M2 TYPE | M3 NAME | M3 TYPE | M4 NAME | M4 TYPE | FORM
					//       0      |         1          |    2   |    3   |  4  |     5     |     6     |     7     |       8      |    9    |    10   |    11   |    12   |    13   |    14   |    15   |    16   |    17   |  18
					// ABILITY: 19 | MOVESET: etc
					mon_disp_name = values[0];
					id_string = values[1];
					type1 = values[2];
					type2 = values[3];
					abilities = [values[5], values[6], values[7]];
					ratio = parseInt(values[8]);
					item_id = values[9];
					moves = [values[10], values[12], values[14], values[16]];
					move_types = [values[11], values[13], values[15], values[17]];
					num = values[4];
					id = id_string.split("-")[0]+"#"+values[18];
					a_selected = values[19];
					mon_level = values[20];
					
					console.log("updating number "+String(num)+" with species "+mon_disp_name);
					var mon_data_name = mon_disp_name;
					matches = $("#species_"+num+" option").filter(function() {
					   return ($(this).data("id") === id+"#"+String(num));
					});
					if (matches.length == 1)
					{
						match = true;
						mon_data_name = matches.val();
					}
					console.log(mon_data_name);
					$("#"+String(num)+" .species_dropdown[id="+String(num)+"]").data("id", id+"#"+String(num)).data("name", mon_data_name).val(mon_data_name);
					
					// UPDATE MON
					e_pfx = "#"+parseInt(num)+" "
					if (!mon_level) { mon_lvl = 100; }
					else { mon_lvl = parseInt(mon_level); }
					$(e_pfx+".mon_name").text(mon_disp_name);
					$(e_pfx+".gendersprite").css("left", String($(e_pfx+".mon_name").width()+14)+"px");
					$(e_pfx+".lvl").text(" Lv. "+String(mon_lvl))
					$(e_pfx+".level_input").val(parseInt(mon_lvl));
					// GENDERS
					$(e_pfx+".gender_dropdown option").remove();
					if (ratio != 8 && ratio != -1) // male
					{
						$(e_pfx+".gender_dropdown").append($('<option>', {
							value: "M"+"#"+parseInt(num),
							text: "Male",
						}));
					}
					$(e_pfx+".gendersprite").attr("src", "../static/img/gender/m.png");
					if (ratio != 0 && ratio != -1) // female
					{
						$(e_pfx+".gender_dropdown").append($('<option>', {
							value: "F"+"#"+parseInt(num),
							text: "Female",
						}));
					}
					if (ratio == 8) { $(e_pfx+".gendersprite").attr("src", "../static/img/gender/f.png"); }
					if (ratio == -1) // genderless
					{
						$(e_pfx+".gender_dropdown").append($('<option>', {
							value: "X"+"#"+parseInt(num),
							text: "Genderless",
						}));
					}
					
					var gender = genders[parseInt(num)-1];
					//console.log(mons[parseInt(num)]);
					console.log(ratio);
					if (ratio == -1)
					{
						$(e_pfx+".gendersprite").css("display", "none");
						$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18)+"px");
						$(e_pfx+".gender_dropdown[id="+num+"]").val("X#"+num);
					}
					else
					{
						if (gender != "X")
						{
							$(e_pfx+".gendersprite").attr("src", "../static/img/gender/"+gender.toLowerCase()+".png");
							$(e_pfx+".gendersprite").css("display", "inline");
							$(e_pfx+".gender_dropdown[id="+num+"]").val(gender+"#"+num);
						}
						$(e_pfx+".lvl").css("left", String($(e_pfx+".mon_name").width()+18+36)+"px");
						$(e_pfx+".gendersprite").css("display", "inline");
					}
					$(e_pfx+".monsprite").attr("src", "../static/img/species/"+id_string+".png");
					// TYPES
					$(e_pfx+".type1").attr("src", "../static/img/typebars/"+String(type1)+".png");
					if (parseInt(type2) != -1)
					{
						$(e_pfx+".type2").attr("src", "../static/img/typebars/"+String(type2)+".png");
						$(e_pfx+".type2").css("visibility", "visible/inherit");
					}
					else
					{
						$(e_pfx+".type2").css("visibility", "hidden");
					}
					// ABILITIES
					a_selected = a_selected.replace(" (Spectrier)", "").replace(" (Glastrier)", "");
					console.log(abilities);
					$(e_pfx+".ability_dropdown option").remove();
					$(e_pfx+".ability_dropdown").append($('<option>', {
						value: abilities[0]+"#"+String(num),
						text: abilities[0],
					}));
					if (abilities[1]) {
						$(e_pfx+".ability_dropdown").append($('<option>', {
							value: abilities[1]+"#"+String(num),
							text: abilities[1]
						}));
					}
					if (abilities[2]) {
						$(e_pfx+".ability_dropdown").append($('<option>', {
							value: abilities[2]+"#"+String(num),
							text: abilities[2]
						}));
					}
					if (abilities.includes(a_selected))
					{
						$(e_pfx+".ability_dropdown").val(a_selected+"#"+String(num));
						$(e_pfx+".ability_name").text(a_selected);
					}
					else
					{
						$("#nomoves").before($('<div>', {
							class: "warn_box",
							id: "invalidability",
							style: "background-color: #ff8329; line-height: 26px; border: 2px solid #341b08",
							text: "Invalid ability for "+mons[parseInt(num)-1]["name"]+": "+a_selected,
						}));
						$(e_pfx+".ability_dropdown").val(abilities[0]+"#"+String(num));
						$(e_pfx+".ability_name").text(abilities[0]);
					}
					//
					
					// UPDATE MOVESET
					
					// invalid move handler
					
					invalid_move_names = "";
					move_names = mons[parseInt(num)-1]["moves"];
					for (var move of move_names)
					{
						learnset_checker = pack.split("#"+move+"#");
						if (learnset_checker.length - 1 < 1) // invalid move
						{
							invalid_move_names += move + ", ";
						}
					}
					if (invalid_move_names.length > 0)
					{
						plural = "";
						if (invalid_move_names.split(",").length > 2)
						{
							plural = "s";
						}
						$("#nomoves").before($('<div>', {
							class: "warn_box",
							id: "invalidmove",
							style: "background-color: #ff8329; line-height: 26px; border: 2px solid #341b08",
							text: "Invalid move"+plural+" for "+mons[parseInt(num)-1]["name"]+": "+invalid_move_names.slice(0, -2),
						}));
					}
					
					slot = 1;
					for (slot = 1; slot <= 4; slot++)
					{
						dropdown = $(e_pfx+".move_dropdown_"+String(slot)+"[id="+String(num)+"]");
						if (slot == 0) { dropdown.data("prev_move", values[22]+"#"+String(slot)+"#"+String(num)); } // prev move for first slot
						else { dropdown.data("prev_move", "-1#"+String(slot)+"#"+String(num)); } // prev move for other slots
						$(e_pfx+".move_dropdown_"+String(slot)+"[id="+String(num)+"] option").remove();
						if (slot != 1)
						{
							dropdown.append($('<option>', {
									value: String(-1)+"#"+String(slot)+"#"+String(num),
									text: "(no move)",
								}));
						}
						for (i = 0; i < (values.length-21)/2; i++)
						{
							dropdown.append($('<option>', {
								value: values[(2*i)+1+21]+"#"+String(slot)+"#"+String(num),
								text: values[(2*i)+21],
							}));
						}
						
						console.log(moves[slot-1]+"#"+String(slot)+"#"+String(num));
						$("#"+String(num)+" .move_dropdown_"+String(slot)+"[id="+String(num)+"]").val(moves[slot-1]+"#"+String(slot)+"#"+String(num));
					}
					
					updateMove(1, num);
					updateMove(2, num);
					updateMove(3, num);
					updateMove(4, num);
					
					//
					
					if (item_id.split("|")[0] != "invalid")
					{
						$("#"+String(num)+" .item_dropdown").val(item_id+"#"+String(num));
						updateItem(num);
					}
					else
					{
						$("#nomoves").before($('<div>', {
							class: "warn_box",
							id: "invaliditem",
							style: "background-color: #ff8329; line-height: 26px; border: 2px solid #341b08",
							text: "Invalid item name: '"+item_id.slice(8,item_id.length)+"'",
						}));
						$("#"+String(num)+" .item_dropdown").val("-1#"+String(num));
						updateItem(num);
					}
				}
			}
		});
	}
	var multi = "";
	var tense = "s";
	if (no_move_text.length > 3) { multi = "s"; tense = "ve";}
	if (no_move_text.length > 0)
	{
		$("#nomoves").text("Slot"+multi+" "+no_move_text.slice(0, -2)+" ha"+tense+" no moves").css("border", "2px solid #341b08");
	}
	else
	{
		$("#nomoves").text("").css("border", "0px");
	}
	if (no_ability_text.length > 3) { multi = "s"; tense = "ve"; }
	else { multi = ""; tense = "s"; }
	if (no_ability_text.length > 0)
	{
		$("#noability").text("Slot"+multi+" "+no_ability_text.slice(0, -2)+" ha"+tense+" no ability (first ability assumed)").css("border", "2px solid #3f3500");
	}
	else
	{
		$("#noability").text("").css("border", "0px");
	}
}

function updateAvatar() {
	name = $(".avatar_dropdown option:selected").val();
	if (name) { $(".avatar").attr("src", "../static/img/avatars/"+name+".png"); }
	else { $(".avatar").removeAttr("src"); }
}

function addSlot() {
	team_size++;
	if (team_size > 6) { team_size = 6; }
	$("#"+team_size+" .ui_cell").css("visibility", "visible");
	if (team_size > 2)
	{
		$("#"+(team_size-1)+" .ui_cell .remove_button").css("display", "none");
	}
	$("#"+team_size+" .ui_cell .remove_button").css("display", "inline");
	$("#"+team_size+" .add_overlay").css("visibility", "hidden");
	$(".monbox[id="+(team_size+1)+"]").css("display", "table");
	$("#"+(team_size+1)+" .ui_cell").css("visibility", "hidden");
	$("#"+(team_size+1)+" .add_overlay").css("visibility", "visible");
	//if ($(document).height() < $(window).height())
	//{
	//	$(".details").css("position", "absolute");
	//}
	//else
	//{
	//	$(".details").css("position", "relative");
	//}
}

function removeSlot() {
	team_size--;
	if (team_size < 1) { team_size = 1; }
	if (team_size > 1)
	{
		$("#"+team_size+" .ui_cell").css("visibility", "visible");
		$("#"+team_size+" .add_overlay").css("visibility", "hidden");
		$("#"+team_size+" .ui_cell .remove_button").css("display", "inline");
	}
	$(".monbox[id="+(team_size+2)+"]").css("display", "none");
	$("#"+(team_size+1)+" .ui_cell").css("visibility", "hidden");
	$("#"+(team_size+1)+" .add_overlay").css("visibility", "visible");
}

function exportTeam() {
	export_string = "";
	for (i = 1; i <= team_size; i++)
	{
		export_string += $("#"+i+" .species_dropdown[id="+i+"]").data("name");
		if ($("#"+i+" .gender_dropdown[id="+i+"] option:selected").attr("value").slice(0,1) != "X") // GENDER
		{
			export_string += " ("+$("#"+i+" .gender_dropdown[id="+i+"] option:selected").attr("value").slice(0,1)+")";
		}
		if ($("#"+i+".item_dropdown[id="+i+"] option:selected").attr("value").split("#")[0] != -1) // ITEM
		{
			export_string += " @ "+$("#"+i+".item_dropdown[id="+i+"] option:selected").text();
		}
		export_string += "\nAbility: "+$("#"+i+".ability_dropdown[id="+i+"] option:selected").text()+"\n";
		export_string += "Level: "+$("#"+i+" .level_input").val()+"\n";
		break_moves = false;
		for (j = 1; j <= 4; j++)
		{
			if (!break_moves)
			{
				move_value = $("#"+i+" .move_dropdown_"+j+"[id="+i+"] option:selected").attr("value").split("#")[0];
				if (move_value != -1)
				{
					export_string += "- " + $("#"+i+" .move_dropdown_"+j+"[id="+i+"] option:selected").text()+"\n";
				}
				else
				{
					break_moves = true;
				}
			}
		}
		export_string += "\n";
	}
	$(".export_text").val(export_string.slice(0, -1));
}

function copyTeam() {
	navigator.clipboard.writeText($(".export_text").val());
}