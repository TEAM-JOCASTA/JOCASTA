

#clonning repo 
RUN git clone https://github.com/TEAM-JOCASTA/JOCASTA-PLUGING.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","./TEAM-JOCASTA/start.sh"]
