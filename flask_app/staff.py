import numpy as np 
import cv2 


def get_results(results):
    detections_list = []
    
    for result in results[0]: 
        bbox = result.boxes.xyxy.cpu().numpy()
        confidence = result.boxes.conf.cpu().numpy()
        merged_detection = [bbox[0][0], bbox[0][1], bbox[0][2], bbox[0][3], confidence[0]]
        detections_list.append(merged_detection)
        
    return np.array(detections_list)

def draw_bounding_boxes_with_id(img, bboxes, ids):
    for bbox, id_ in zip(bboxes, ids):
        cv2.rectangle(img,(int(bbox[0]), int(bbox[1])),(int(bbox[2]), int(bbox[3])),(0,0,255),2)
        cv2.putText(img, "ID: " + str(id_), (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)       
    return img

