import cv2
import numpy as np

drawing =                       False
first_point =                   None
second_point =                  None
img =                           None
temp_img =                      None
history =                       []  

##### CASTRO 11/03/2026 - ALGUNS PARÂMETROS BEM SIMPLES PARA FACILITAR A VISUALIZAÇÃO
espessura_linha_vermelha =      1
espessura_linha_verde =         2
comprimento_linha_vermelha =    50
taamanho_do_texto =             0.5
distancia_entre_textos_X_e_Y =  10

def draw_perpendicular_line(image, point, direction_point, length, color, thickness):

    dx,dy = direction_point[0] - point[0], direction_point[1] - point[1]
    
    if dx == 0 and dy == 0:
        angle = 0
    else:
        angle = np.atan2(dy, dx)
    
    perp_angle = angle + np.pi/2
    
    x1, y1 = int(point[0] + length * np.cos(perp_angle)), int(point[1] + length * np.sin(perp_angle))
    x2, y2 = int(point[0] - length * np.cos(perp_angle)), int(point[1] - length * np.sin(perp_angle))
    
    cv2.line(image, (x1, y1), (x2, y2), color, thickness,cv2.LINE_AA)

def save_to_history():
    
    global img, history
    history.append(img.copy())
    
    if len(history) > 20:  
        
        history.pop(0)

def undo_last():
    
    global img, temp_img, history, first_point, second_point, drawing
    if history:
        img =           history.pop()  
        temp_img =      img.copy()
        first_point =   None
        second_point =  None
        drawing =       False
        return True
    return False

def mouse_callback(event, x, y, flags, param):
    global drawing, first_point, second_point, img, temp_img
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing =           True
        first_point =       (x, y)
        second_point =      None
        temp_img =          img.copy()
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            second_point = (x, y)
            temp_img = img.copy()
            current_pos = (f'origem: {first_point}, fim: {x,y}')
            if first_point[0]== x:
                paralelo_X = 'COLINEAR EM X'
                
                cv2.putText(temp_img, paralelo_X, (10,50),cv2.FONT_HERSHEY_SIMPLEX, taamanho_do_texto, (255, 90, 0), 25,cv2.LINE_AA)
                
            if first_point[1]== y:
                paralelo_X = 'COLINEAR EM Y'
                
                cv2.putText(temp_img, paralelo_X, (10,30),cv2.FONT_HERSHEY_SIMPLEX, taamanho_do_texto, (0, 150, 0), 25,cv2.LINE_AA)

            if first_point and second_point:
                
                cv2.line(temp_img, first_point, second_point, (0, 255, 0), espessura_linha_verde)
                draw_perpendicular_line(temp_img, first_point, second_point, comprimento_linha_vermelha, (0, 0, 255), espessura_linha_vermelha)
                draw_perpendicular_line(temp_img, second_point, first_point, comprimento_linha_vermelha, (0, 0, 255), espessura_linha_vermelha)
                
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            second_point = (x, y)
            if first_point and second_point:
                save_to_history()
                
                cv2.line(img, first_point, second_point, (0, 255, 0), espessura_linha_verde)
                
                draw_perpendicular_line(img, first_point, second_point, comprimento_linha_vermelha, (0, 0, 255), espessura_linha_vermelha)            
                draw_perpendicular_line(img, second_point, first_point, comprimento_linha_vermelha, (0, 0, 255), espessura_linha_vermelha)
                distancia_X = (f'd[x] = {abs(second_point[0]-first_point[0])}')
                distancia_Y = (f'd[y] = {abs(second_point[1]-first_point[1])}')
                cv2.putText(img, distancia_X, (int(second_point[0]+comprimento_linha_vermelha-10), int(second_point[1] - distancia_entre_textos_X_e_Y)),cv2.FONT_HERSHEY_SIMPLEX, taamanho_do_texto, (255,90, 0), 1,cv2.LINE_AA,)
                cv2.putText(img, distancia_Y, (int(second_point[0]+comprimento_linha_vermelha-10), int(second_point[1] + distancia_entre_textos_X_e_Y)),cv2.FONT_HERSHEY_SIMPLEX, taamanho_do_texto, (0, 255, 0), 1,cv2.LINE_AA)
                print('LINE: ',distancia_X, distancia_Y)
                
                temp_img = img.copy()
            drawing = False

def main():
    global img, temp_img, first_point, second_point, drawing, history
    
    img = np.zeros((600, 800, 3), dtype=np.uint8)
    temp_img = img.copy()
    history = []  
    
    cv2.namedWindow('Draw Line')
    cv2.setMouseCallback('Draw Line', mouse_callback)
    
    while True:
        cv2.imshow('Draw Line', temp_img)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('c'):
            
            #undo_last()
            answer = input('>>> DESEJA APAGAR TODAS AS LINHAS? (PRESSIONE ENTER PARA CONFIRMAR EXCLUSÃO OU TECLE N PARA CANCELAR A OPERÇÃO)')
            if answer == '':
                    save_to_history()
                    ##### CASTRO 11/03/2026 - ISSO VAI HERDAR PARÂMETROS DE WIDTH/HEIGHT DA CÂMERA DPS
                    img = np.zeros((600, 800, 3), dtype=np.uint8)
                    temp_img =      img.copy()
                    first_point =   None
                    second_point =  None
                    drawing =       False
                    print('>>> OPERAÇÃO CONCLUÍDA')
            elif answer == 'n' or answer == 'N':
                    print('>>> OPERAÇÃO CONCLUÍDA')
            
            
        elif key == ord('u'):  
            #undo_last()
            answer = input('>>> DESEJA APAGAR A ÚLTIMA LINHA? (PRESSIONE ENTER PARA CONFIRMAR EXCLUSÃO OU TECLE N PARA CANCELAR A OPERÇÃO)')
            if answer == '':
                if undo_last():
                    print('>>> OPERAÇÃO CONCLUÍDA')
            elif answer == 'n' or answer == 'N':
                    print('>>> OPERAÇÃO CONCLUÍDA')
    
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()