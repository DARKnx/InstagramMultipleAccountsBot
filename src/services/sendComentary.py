import time, random


def run(self):
    driver = self.driver
    message = self.message 
    commentarys = 0

    try:

    
        for i in range(0, 5):

            driver.find_element_by_class_name("_ablz").click()
            time.sleep(random.randint(1, 5) / 30)
            driver.find_element_by_class_name("_ablz").send_keys(str(self.commentsSent + commentarys) + ' ' + message)
            time.sleep(random.randint(1, 5) / 30)
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div").click()
            commentarys  += 1
            print(commentarys, ' - Comentario adicionado')
            time.sleep(random.randint(3, 7))

    except:
        return print('[' + self.username + '] - Erro ao adicionar comentario')
    return commentarys