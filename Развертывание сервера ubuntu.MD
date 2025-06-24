### 1. Обновляем пакеты
``````
sudo apt update && sudo apt upgrade -y
``````
### 2. Установка MC
``````
 sudo apt-get install mc
``````

### 3. Устанавливаем зависимости
`````
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
`````

### 4. Добавляем GPG-ключ Docker
`````
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
`````

### 5. Добавляем репозиторий Docker
``````
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
``````

### 6. Устанавливаем Docker
``````
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
``````

### 7. Проверяем установку
`````
sudo docker --version
`````

### 8. Добавляем текущего пользователя в группу docker
``````
sudo usermod -aG docker $USER
``````

### 9. Применяем изменения (или перезайдите в систему)
`````
newgrp docker
`````

### 10. Скачиваем бинарник Docker Compose
`````
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
`````

### 11. Даем права на выполнение
`````
sudo chmod +x /usr/local/bin/docker-compose
`````

### 12. Проверяем установку
`````
docker-compose --version
`````

### 13. Автозапуск Docker при загрузке
`````
sudo systemctl enable docker
`````

### 14. Проверка статуса
`````
sudo systemctl status docker
`````
