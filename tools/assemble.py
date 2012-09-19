# An assembler for aether9
sdoc = params["INPUT"]
tdoc = params["OUTPUT"]
sinfo = pdf_info.extract(sdoc)
bbox = sinfo["page_size"][0][1]
pcount = sinfo["page_count"]
swidth = bbox["width"]
twidth =  2 * swidth
height = bbox["height"]

imposition_plan = []

belle_page = True

bp_offsetL = 7
bp_offsetR = -16

up_offsetL = 16
up_offsetR = -7

full_page_image = [
	27,
	39,
	40,
	49,
	74,
	84,
	96,
	97,
	101,
	107,
	109,
	110,
	118,
	119,
	]

target_page = 0
for i in range(0,pcount,2):
	print('P %d'%(target_page))
	if belle_page:
		target_page += 1
		bp_offsetR_c = bp_offsetR
		if target_page in full_page_image:
			print('Alter offset for page [B] %d'%(i+1,))
			bp_offsetR_c = bp_offsetL
			
		imposition_plan.append({
			"target_document" : tdoc,
			"target_page_width" : twidth,
			"target_page_height" : height,
			"pages" : [
				{
				"source_document" : sdoc,
				"source_page" : i,
				"crop_box" : {"left":0,"bottom":0,"width":swidth, "height":height},
				"translate" : [0 + bp_offsetL,0],
				"rotate" : 0,
				"scale" : [1,1]
				},
				{
				"source_document" : sdoc,
				"source_page" : i + 1,
				"crop_box" : {"left":0,"bottom":0,"width":swidth, "height":height},
				"translate" : [swidth + bp_offsetR_c , 0],
				"rotate" : 0,
				"scale" : [1,1]
				}
				]
		})
		belle_page = False
	else:
		
		target_page += 1
		up_offsetL_c = up_offsetL
		if target_page in full_page_image:
			print('Alter offset for page [U] %d'%(i+2,))
			up_offsetL_c = up_offsetR
			
		imposition_plan.append({
			"target_document" : tdoc,
			"target_page_width" : twidth,
			"target_page_height" : height,
			"pages" : [
				{
				"source_document" : sdoc,
				"source_page" : i,
				"crop_box" : {"left":0,"bottom":0,"width":swidth, "height":height},
				"translate" : [0 + up_offsetL_c,0],
				"rotate" : 0,
				"scale" : [1,1]
				},
				{
				"source_document" : sdoc,
				"source_page" : i + 1,
				"crop_box" : {"left":0,"bottom":0,"width":swidth, "height":height},
				"translate" : [swidth + up_offsetR,0],
				"rotate" : 0,
				"scale" : [1,1]
				}
				]
		})
		belle_page = True
	
