import requests, json






# VKpoc wall post with image(s) and message
def vkpoc_wp_im( vkp_at, vkp_gi, vkp_v, vkp_i, vkp_m ):
# vkpoc_wp_im('access token', 'group id', 'vk api version', (image,), 'Post message')

    #
    vkpoc_rslt = []

    #
    if vkp_i and len(vkpoc_rslt) <= 10:
        for vkpil in vkp_i:

            # get wall upload server
            vkp_image = {'photo': ('vk_photo_image.jpg', open(vkpil, 'rb'))}
            vkp_uurl = 'https://api.vk.com/method/photos.getWallUploadServer?'
            vkp_uresp = json.loads(requests.post(vkp_uurl, dict(access_token=vkp_at, gid=vkp_gi, v=vkp_v)).text)
            vkp_ufresp = json.loads(requests.post(vkp_uresp['response']['upload_url'], files=vkp_image).text)
            vkp_oid = str(vkp_uresp['response']['user_id'])

            # save photo and get id's
            vkp_surl = 'https://api.vk.com/method/photos.saveWallPhoto?'
            vkp_sresp = requests.post(vkp_surl, dict(access_token=vkp_at, gid=vkp_gi, v=vkp_v, photo=vkp_ufresp['photo'], hash=vkp_ufresp['hash'], server=vkp_ufresp['server']))
            vkpoc_rslt.append('photo'+vkp_oid+'_'+str(json.loads(vkp_sresp.text)['response'][0]['id']))

        #
        if len(vkpoc_rslt) >= 1:
            
            #
            vkpil_sres = ','.join(vkpoc_rslt)
            vkp_purl = 'https://api.vk.com/method/wall.post?'
            vkp_presp = json.loads(requests.post(vkp_purl, dict(access_token=vkp_at, owner_id='-'+vkp_gi, v=vkp_v, attachments=vkpil_sres, message=vkp_m)).text)
            vkp_res = vkp_presp['response']['post_id']
            
            #
            if vkp_res:
                return(vkp_res)
            
            #
            else:
                return('info-> post failed')

        #
        else:
            return('info-> empty images list')

    #
    else :
        return('info-> empty images list or more than 10 images ')