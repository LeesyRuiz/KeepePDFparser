# 
import os
import cv2
import numpy

SHOW_IMAGES = True

#region initialization
#  avoid long path names by switching to the img folder
filepath = os.path.dirname(os.path.abspath(__file__))
print('... working folder : {0}'.format(filepath))
os.chdir(filepath)
#endregion

#region opening all the images here. 

print('... Keepe PDF parser...')
img = cv2.imread("civitas.png",0)
# img = cv2.imread("dwellings.png",0)
# img = cv2.imread("cornerstone.png",0)
cv2.imshow('Original WO', img)

tenant_pattern = cv2.imread('template_tenants.png',0)
# cv2.imshow('Tenant', tenant_pattern)

description_pattern =cv2.imread('template_description.png',0)
# cv2.imshow('Description', description_pattern)

details_pattern =cv2.imread('template_details.png',0)
# cv2.imshow('Details', description_pattern)

wo_pattern =cv2.imread('template_wo.png',0)
# cv2.imshow('Work Order', wo_pattern)

#endregion

#region template matching 

# Tenant Pattern
result = cv2.matchTemplate(img, tenant_pattern, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
tenant_x = max_loc[0]
tenant_y = max_loc[1]
# print(max_val,max_loc)

if SHOW_IMAGES:
    cv2.circle(result,max_loc, 15,255,2)
    cv2.imshow("Tenant Matching",result)

# Description Pattern
desc_result = cv2.matchTemplate(img, description_pattern, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(desc_result)
description_x = max_loc[0]
description_y = max_loc[1]
# print(max_val,max_loc)
if SHOW_IMAGES:
    cv2.circle(desc_result,max_loc, 15,255,2)
    cv2.imshow("Description Matching",desc_result)

# Details Pattern
details_result = cv2.matchTemplate(img, details_pattern, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(details_result)
details_x = max_loc[0]
details_y = max_loc[1]
# print(max_val,max_loc)
if SHOW_IMAGES:
    cv2.circle(details_result,max_loc, 15,255,2)
    cv2.imshow("Details Matching",details_result)

# WO Pattern
wo_result = cv2.matchTemplate(img, wo_pattern, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(wo_result)
wo_x = max_loc[0]
wo_y = max_loc[1]
# print(max_val,max_loc)
if SHOW_IMAGES:
    cv2.circle(wo_result,max_loc, 15,255,2)
    cv2.imshow("WO Matching",wo_result)


#endregion

#region cropping the images and getting ready for OCR

# cropping the image after finding the pattern. From the pattern matching to the next section as per the document. 
if (tenant_y <= description_y):
    y1 = tenant_y - 10
    y2 = description_y - 10
else:
    y1 = tenant_y - 10
    y2 = tenant_y + 20

roi_tenant = img[y1:y2, :]
cv2.imshow('Tenant ROI', roi_tenant)


if (description_y <= details_y):
    y1 = description_y - 10
    y2 = details_y - 10
else:
    y1 = description_y - 10
    y2 = description_y + 80
roi_description = img[y1:y2, :]
cv2.imshow('Description ROI', roi_description)

r,c = wo_pattern.shape
roi_wo = img[(wo_y):(wo_y+r), wo_x:]
cv2.imshow('WO ROI', roi_wo)

#endregion

#region cv2 gracefull shutdown
cv2.waitKey(0)
cv2.destroyAllWindows()
#endregion


