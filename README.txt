Hey tutors!

ima write in english again then :)

For task 1 
I had batch size and made another notebook since i found it easier to work with. 
lower batch sizes worked better (more accuracy) for our model 4-16. Other than that differencers were small except for the huge 256 batch size, u can check it in my notebook or just the pictures.

16 checks out for me since we dont want to over generalize as hands as us humans are pretty diverse. Overall it seems like a more straight forward hyperparameter than some others. 
Im excited to learn what the others found out. 

For task 2
I used the website that i also put in the discord for the box. I just made 3 simple monotone fotos as i dont really like taking pictures of myself.
Please Check the conf-matrix.png in file02. only one rock was falsely labled as peace. 

For the implementation i very ugly-ly copied the notebook from 1 and used that model to make the matrix. i thought about cleaning that directory up but if u care about how we came to the matrix i kept it. thought 1 score wasnt thought out for us to doing it to fancy.
my images are in my_custom_dataset and the annotated json file is annot-thomaslucke.json.

For Task 3
i used a notebook again and i feel like it looks quite organized. For the model i used the same from the notebook. For the programm i had some starting problems making it good enough. 
It doesnt have a bbox so i just hardcoded a box with ROI so the model has an area to work with. 
At first i thought it worked pretty bad but after finetuning the variables i think it works well now. 
The most important thing is that ur hand fills out nearly the entire green box for it to work well just like the example pictures from the model. so if its not zoomed in enough it worked far worse. 
i guess we could have made an automatic bbox scanner but i feel like that would be overscope for this programm and would make the latency worse. 
If u want to repeat VOLUME increase or other commands please cycle to no gesture as just holding wont spamm a command. Stop programm with q. 

Thanks :)

worked all friday and saturday to have time for the CSD in tübingen this Sunday. Maybe see you there though it is way to hot and sunny... Happy Pride!

