from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.templatetags.static import static

from .models import Move, Item, Species, Ability

from PIL import Image, ImageFont, ImageDraw
import base64
from tempfile import TemporaryFile

# Create your views here.

def index(request):
    pokemon_data = Species.objects.filter(species_id = 1)[0]
    if request.method == 'GET':
        #selection = request.GET.get('id', None)
        #if selection:
        if request.GET.get('mon_id', False):
            print(request.GET.get('mon_id'))
            pokemon_data = Species.objects.filter(species_id = request.GET.get('mon_id'))[0]
    debug = request.GET.get('species_dropdown')
    mons = Species.objects.all()
    items = Item.objects.all()
    id_string = str(pokemon_data.species_id)
    split_string = "-"+pokemon_data.species_form_name.title()
    if split_string != "-":
    #    split_string = ""
        mon_disp_name = pokemon_data.species_name[:-len(split_string)]
    else:
        mon_disp_name = pokemon_data.species_name
    type_1 = pokemon_data.species_type_1
    type_2 = pokemon_data.species_type_2
    if pokemon_data.species_form_name != "":
        id_string += "-" + "".join(pokemon_data.species_form_name.lower().split("-"))
    abilities = []
    abilities.append(Ability.objects.filter(ability_id = pokemon_data.species_ability_1)[0].ability_name)
    if (pokemon_data.species_ability_2):
        abilities.append(Ability.objects.filter(ability_id = pokemon_data.species_ability_2)[0].ability_name)
    if (pokemon_data.species_ability_3):
        abilities.append(Ability.objects.filter(ability_id = pokemon_data.species_ability_3)[0].ability_name)
    avatar_names = [
            "Allister", "Artist", "Avery", "Backpacker", "Ballonlea Gym", "Bea", "Beauty", "Bede", "Black Belt",
            "Cabbie", "Café Master", "Cameraman", "Champion Cup", "Circhester Gym (Gordie)", "Circhester Gym (Melony)",
            "Cook", "Dancer", "Doctor (Female)", "Doctor (Male)", "Eevee", "Fisher", "Galar League (Champion)",
            "Galar League", "Galarian Star Tournament", "Gentleman", "Gordie", "Grookey", "Hammerlocke Gym", "Hiker",
            "Hop", "Hulbury Gym", "Kabu", "Klara", "Lass", "League Staff (Female)", "League Staff (Male)", "Leon",
            "Madame", "Marnie", "Master Dojo", "Melony", "Milo", "Model", "Motostoke Gym", "Musician", "Mustard",
            "Nessa", "Office Worker (Female)", "Office Worker (Male)", "Opal", "Peony Expedition Company", "Peony",
            "Piers", "Pikachu", "Poison Gym", "Poké Kid (Female)", "Poké Kid (Male)", "Pokémon Breeder (Female)",
            "Pokémon Breeder (Male)", "Police Officer", "Postman", "Psychic Gym", "Question Mark", "Raihan",
            "Rail Staff", "Reporter", "Schoolboy", "Schoolgirl", "Scorbunny", "Shielbert", "Sobble", "Spikemuth Gym",
            "Stow-on-Side Gym (Allister)", "Stow-on-Side Gym (Bea)", "Swimmer (Female)", "Swimmer (Male)", "Swordward",
            "Team Yell", "Turffield Gym", "Worker (Female)", "Worker (Male)", "Youngster"
        ]
    context = {
        'pokemon_data': pokemon_data,
        'id_string': id_string,
        'disp_name': mon_disp_name,
        'type_1': type_1,
        'type_2': type_2,
        'debug': debug,
        'mons': mons.order_by('species_name'),
        'items': items.order_by('item_name'),
        'abilities': abilities,
        'moveset': pokemon_data.learnset.order_by('move_name').all(),
        'firstmove': pokemon_data.learnset.order_by('move_name')[0],
        'avatars': avatar_names,
    }
    return render(request, 'viz/index.html', context)

def monLookup(request):
    if request.method =='GET':
        mon_name = request.GET.get('mon_name')
        mon_name = mon_name.replace("’", "'").replace("-Gmax", "")
        pokemon_data = Species.objects.filter(species_name = mon_name)
        if (pokemon_data.count() < 1):
            pokemon_data = Species.objects.filter(species_name__contains = mon_name)
        else:
            pokemon_data = Species.objects.filter(species_name = mon_name)
        if not pokemon_data:
            return HttpResponse("invalid species#"+str(request.GET.get('mon_counter'))+"#"+request.GET.get('mon_name'))
        else:
            pokemon_data = pokemon_data[0]
        item = "-1"
        if request.GET.get('mon_item') != "-1":
            item = Item.objects.filter(item_name = request.GET.get('mon_item'))
            if not item:
                item = "invalid|"+request.GET.get('mon_item')
            else:
                item = item[0].item_id
        moves = [
            request.GET.get('move_1'),
            request.GET.get('move_2'),
            request.GET.get('move_3'),
            request.GET.get('move_4')
        ]
        moves_redupe = []
        [moves_redupe.append(x) for x in moves if x not in moves_redupe]
        moves = moves_redupe
        while (len(moves) < 4):
            moves.append("")
        movestring = ""
        for move in moves:
            if move != "":
                move_obj = Move.objects.filter(move_name = move)
                if not move_obj:
                    movestring += ""
                else:
                    if move_obj[0] in pokemon_data.learnset.all():
                        movestring += "#"+str(move_obj[0].move_id)+"#"+str(move_obj[0].move_type_id)
                    else:
                        movestring += ""
            else:
                movestring += ""
        movestring_checker = movestring.split("#")
        print(movestring_checker)
        if len(movestring_checker) <= 1:
            new_move_1 = pokemon_data.learnset.order_by('move_name')[0]
            movestring = "#"+str(new_move_1.move_id)+"#"+str(new_move_1.move_type_id)+"#-1##-1##-1#"
        else:
            while len(movestring_checker) < 9:
                movestring += "#-1#"
                movestring_checker = movestring.split("#")
        print(movestring)
        num = request.GET.get('mon_counter')
        ###########################
        split_string = "-"+pokemon_data.species_form_name.title()
        if split_string != "-":
            mon_disp_name = pokemon_data.species_name[:-len(split_string)]
        else:
            mon_disp_name = pokemon_data.species_name
        id_string = str(pokemon_data.species_id)
        if pokemon_data.species_form_name != "":
            id_string += "-" + "".join(pokemon_data.species_form_name.lower().split("-"))
        type_1 = pokemon_data.species_type_1
        type_2 = pokemon_data.species_type_2
        if not type_2: type_2 = -1
        a1 = Ability.objects.filter(ability_id = pokemon_data.species_ability_1)[0].ability_name
        if (pokemon_data.species_ability_2):
            a2 = Ability.objects.filter(ability_id = pokemon_data.species_ability_2)[0].ability_name
        else: a2 = ""
        if (pokemon_data.species_ability_3):
            a3 = Ability.objects.filter(ability_id = pokemon_data.species_ability_3)[0].ability_name
        else: a3 = ""
        ratio = pokemon_data.species_gender_ratio
        monstring = mon_disp_name+"#"+id_string+"#"+str(type_1)+"#"+str(type_2)+"#"+num+"#"+a1+"#"+a2+"#"+a3+"#"+str(ratio)
        moveset_string = ""
        for move in pokemon_data.learnset.order_by('move_name'):
            moveset_string += "#"+move.move_name+"#"+str(move.move_id)
        #return HttpResponse(str(mon.species_id)+"#"+mon.species_form_name+"#"+str(item)+movestring+"#"+num)
        a_selected = request.GET.get("mon_ability")
        if a_selected == "": a_selected = a1;
        mon_level = request.GET.get("mon_level")
        if not mon_level: mon_level = ""
        return HttpResponse(monstring+"#"+str(item)+movestring+"#"+pokemon_data.species_form_name+"#"+a_selected+"#"+mon_level+moveset_string)
    return HttpResponse("Error in mon lookup request (not GET)")

def updateMon(request):
    if request.method == 'GET':
        print(request.GET)
        #if request.GET.get('mon_id', False):
        print(request.GET.get('mon_id'))
        values = request.GET.get('mon_id').split("#")
        if values[1]:
            pokemon_data = Species.objects.filter(species_id = int(values[0]), species_form_name = values[1])[0]
        else:
            pokemon_data = Species.objects.filter(species_id = int(values[0]))[0]
        id_string = str(pokemon_data.species_id)
        split_string = "-"+pokemon_data.species_form_name.title()
        print(split_string)
        if split_string != "-":
            mon_disp_name = pokemon_data.species_name[:-len(split_string)]
        else:
            mon_disp_name = pokemon_data.species_name
        if pokemon_data.species_form_name != "":
            id_string += "-" + "".join(pokemon_data.species_form_name.lower().split("-"))
        type_1 = pokemon_data.species_type_1
        type_2 = pokemon_data.species_type_2
        if not type_2: type_2 = -1
        a1 = Ability.objects.filter(ability_id = pokemon_data.species_ability_1)[0].ability_name
        if (pokemon_data.species_ability_2):
            a2 = Ability.objects.filter(ability_id = pokemon_data.species_ability_2)[0].ability_name
        else: a2 = ""
        if (pokemon_data.species_ability_3):
            a3 = Ability.objects.filter(ability_id = pokemon_data.species_ability_3)[0].ability_name
        else: a3 = ""
        ratio = pokemon_data.species_gender_ratio
        return HttpResponse(mon_disp_name+"#"+id_string+"#"+str(type_1)+"#"+str(type_2)+"#"+str(values[2])+"#"+a1+"#"+a2+"#"+a3+"#"+str(ratio))
    return HttpResponse("Error in mon update request method (not GET)")

def updateItem(request):
    if request.method == 'GET':
        values = request.GET.get('item_id').split("#")
        if int(values[0]) != -1:
            item_data = Item.objects.filter(item_id = int(values[0]))[0]
            return HttpResponse(item_data.item_name+"#"+str(item_data.item_id)+"#"+str(values[1]))
        else:
            return HttpResponse("#-1#"+str(values[1]))
    return HttpResponse("Error in item update request method (not GET)")

def updateMove(request):
    if request.method == 'GET':
        values = request.GET.get('move_id').split("#")
        # move id, slot number, mon number
        if int(values[0]) != -1:
            move = Move.objects.filter(move_id = int(values[0]))[0]
            move_name = move.move_name
            move_type = move.move_type_id
            return HttpResponse(move_name+"#"+str(move_type)+"#"+values[1]+"#"+values[2])
        else:
            return HttpResponse("##"+values[1]+"#"+values[2])
    return HttpResponse("Error in move update request method (not GET)")

def updateMoveset(request):
    if request.method == 'GET':
        values = request.GET.get('mon_id').split("#")
        if values[1]:
            pokemon_data = Species.objects.filter(species_id = int(values[0]), species_form_name = values[1])[0]
        else:
            pokemon_data = Species.objects.filter(species_id = int(values[0]))[0]
        moveset_string = str(values[2])
        for move in pokemon_data.learnset.order_by('move_name'):
            moveset_string += "#"+move.move_name+"#"+str(move.move_id)
        return HttpResponse(moveset_string)
    return HttpResponse("Error in moveset update request method (not GET)")

def makeImage(request):
    if request.method == 'GET':
        bg = Image.open('static/img/ui/bg.png', 'r').convert('RGBA')
        img = Image.new('RGBA', (1920, 1080), (255, 255, 255, 0))
        img.paste(bg, (0, 0))
        img_draw = ImageDraw.Draw(img)
        bg.close()
        tpo = (120, 28) # top panel offset
        kakugo = ImageFont.truetype('static/css/fot-kakugo.ttf', 26)
        for mon in range(1, int(request.GET.get("team_size"))+1):
            tpo = (120 + (880*(1-(mon%2))), 28+(280*int((mon-1)/2)))
            img_draw.rectangle([tpo, (tpo[0]+410, tpo[1]+263)], fill="#009da4", outline=None)
            img_draw.rectangle([(tpo[0]+410, tpo[1]), (tpo[0]+410+389, tpo[1]+263)], fill="#f0f0f0", outline=None)
            values = request.GET.get('species_id_'+str(mon)).split("#")
            id_string = str(values[0])
            if values[1] != "":
                id_string += "-" + "".join(values[1].lower().split("-"))
            m_spr = Image.open('static/img/species/'+id_string+'.png', 'r')
            spr_w, spr_h = m_spr.size
            m_spr_2x = m_spr.resize((spr_w*2, spr_h*2), Image.NEAREST)
            img.paste(m_spr_2x, (tpo[0]+67-spr_w+2, tpo[1]+103-(spr_h*2)-6), m_spr_2x.convert('RGBA'))
            m_spr.close()
            if values[1]:
                pokemon_data = Species.objects.filter(species_id = int(values[0]), species_form_name = values[1])[0]
            else:
                pokemon_data = Species.objects.filter(species_id = int(values[0]))[0]
            split_string = "-"+pokemon_data.species_form_name.title()
            if split_string != "-":
                mon_disp_name = pokemon_data.species_name[:-len(split_string)]
            else:
                mon_disp_name = pokemon_data.species_name
            img_draw.text((tpo[0]+10, tpo[1]+107), mon_disp_name, (255, 255, 255), font=kakugo)
            gender = request.GET.get('gender_'+str(mon)).lower()
            g_offset = 0
            #name_offset = request.GET.get('name_width_'+str(mon))
            name_offset = kakugo.getmask(mon_disp_name).getbbox()[2]
            if gender != "x":
                g_spr = Image.open('static/img/gender/'+gender+'.png', 'r').convert('RGBA')
                g_offset += g_spr.size[0] + 5
                #img.paste(g_spr, (tpo[0]+15+int(name_offset), tpo[1]+115), g_spr.convert('RGBA'))
                img = Image.alpha_composite(img, a_comp_offset(img, g_spr, (tpo[0]+15+int(name_offset), tpo[1]+115)))
                img_draw = ImageDraw.Draw(img)
                g_spr.close()
            level = request.GET.get('level_'+str(mon))
            img_draw.text((tpo[0]+name_offset+15+g_offset, tpo[1]+107), "Lv. "+level, (255, 255, 255), kakugo)
            ability = request.GET.get('ability_'+str(mon)).split('#')[0]
            img_draw.text((tpo[0]+10, tpo[1]+202-43-2), ability, (255, 255, 255), kakugo)
            t1 = pokemon_data.species_type_1
            t2 = pokemon_data.species_type_2
            t1_spr = Image.open('static/img/typebars_rounded/'+str(t1)+'.png', 'r').convert('RGBA')#.resize((200, 42), Image.BICUBIC)
            #img.paste(t1_spr, (tpo[0]+184, tpo[1]+6), t1_spr)
            img = Image.alpha_composite(img, a_comp_offset(img, t1_spr, (tpo[0]+184, tpo[1]+6)))
            img_draw = ImageDraw.Draw(img)
            t1_spr.close()
            if t2:
                t2_spr = Image.open('static/img/typebars_rounded/'+str(t2)+'.png', 'r').convert('RGBA')#.resize((200, 42), Image.BICUBIC)
                #img.paste(t2_spr, (tpo[0]+184, tpo[1]+59), t2_spr)
                img = Image.alpha_composite(img, a_comp_offset(img, t2_spr, (tpo[0]+184, tpo[1]+58)))
                img_draw = ImageDraw.Draw(img)
                t2_spr.close()
            item_id = request.GET.get('item_'+str(mon)).split("#")[0]
            if item_id != "-1":
                item = Item.objects.filter(item_id = item_id)[0]
                img_draw.text((tpo[0]+10, tpo[1]+211-2), item.item_name, (255, 255, 255), kakugo)
                i_spr = Image.open('static/img/items/'+item_id+'.png', 'r')
                spr_w, spr_h = i_spr.size
                i_spr_2x = i_spr.resize((spr_w*2, spr_h*2), Image.NEAREST)
                img.paste(i_spr_2x, (tpo[0]+94+2, tpo[1]+44-6), i_spr_2x.convert('RGBA'))
                i_spr.close()
            move_lockout = False
            for i in range(1, 5):
                if not move_lockout:
                    get_id = request.GET.get('move_'+str(i)+'_'+str(mon)).split("#")[0]
                    if get_id != "-1":
                        move = Move.objects.filter(move_id = get_id)[0]
                        img_draw.text((tpo[0]+408+68, tpo[1]+11+((i-1)*64)), move.move_name, (0, 0, 0), font=kakugo)
                        mt_spr = Image.open('static/img/typeicons/'+str(move.move_type_id)+'.png', 'r').convert('RGBA')
                        #img.paste(mt_spr, (tpo[0]+408+4, tpo[1]+3+((i-1)*64)), mt_spr.convert('RGBA'))
                        img = Image.alpha_composite(img, a_comp_offset(img, mt_spr, (tpo[0]+408+4, tpo[1]+3+((i-1)*64))))
                        img_draw = ImageDraw.Draw(img)
                        mt_spr.close()
                    else:
                        move_lockout = True
        avatar = request.GET.get('avatar')
        if avatar:
            av_sprite = Image.open('static/img/avatars/'+avatar+'.png', 'r').crop((0, 0, 256, 256)).resize((129, 129), Image.BICUBIC).convert("RGBA")
            img = Image.alpha_composite(img, a_comp_offset(img, av_sprite, (375, 875)))
            img_draw = ImageDraw.Draw(img)
            #img = Image.alpha_composite(Image.new("RGBA", img.size), img.convert("RGBA"))
            #img.paste(av_sprite, (376, 876), av_sprite)
        game = request.GET.get('game')
        if game:
            game_sprite = Image.open('static/img/ui/'+game+'.png', 'r').convert("RGBA")
            img = Image.alpha_composite(img, a_comp_offset(img, game_sprite, (1431, 867)))
            img_draw = ImageDraw.Draw(img)
        name = request.GET.get('name')
        nw = kakugo.getmask(name).getbbox()[2]
        img_draw.text((512+((335-nw)/2), 883), name, (255, 255, 255), font=kakugo)
        teamname = request.GET.get('teamname')
        tnw = kakugo.getmask(teamname).getbbox()[2]
        img_draw.text((878+((535-tnw)/2), 883), teamname, (255, 255, 255), font=kakugo)
        watermark = "Generate your own team image at [URL]"
        wmw = kakugo.getmask(watermark).getbbox()[2]
        img_draw.text((512+((900-wmw)/2), 947), watermark, (0, 0, 0), font=kakugo)
        fp = TemporaryFile()
        img.save(fp, "PNG")
        fp.seek(0)
        image_b64 = base64.b64encode(fp.read()).decode('utf-8')
        fp.close()
        return HttpResponse(image_b64)
    return HttpResponse("Error in generating image request method (not GET)")

def a_comp_offset(img, sprite, offset):
    temp_bg_img = Image.new("RGBA", img.size)
    temp_bg_img.paste(sprite, offset, sprite)
    return temp_bg_img
