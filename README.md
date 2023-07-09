further update will come ;)
Getting ready to get your packages to our on-prem army npm repository
We use am open source npm repo called Verdaccio
Verdaccio is a lightweight, private npm proxy registry that you can run on your local network. It allows you to create and manage your own private npm packages

Install Verdaccio globally by running the following command:
npm install -g verdaccio
Start Verdaccio by running the following command:
verdaccio

•	If this doesn’t work you might want to try npx verdaccio

Got to your package.json (server/client) and change the second number on the call function to the line number of your first dependency and the third number to the line right after your last dependency
(the code will be improved for better automation)
Edit the server path and the client path to apply to your project format
Choose the right path for the number you changed
Run the script
After doing that you should see in a path like this one : C:\Users\fadid\.config\verdaccio
 A file named storage
Go back to your project run in terminal
npm i node-tgz-downloader -g
and then run download-tgz package-json package.json on the client/server depends on what you chose earlier (cd to said path and run the command there)
you will get a tarballs folder after this copy all its content and paste it in C:\Users\fadid\.config\verdaccio\storage
make sure – copy its content not as a folder and paste and skip duplications it into the storage folder
and now your are good to go, all you need to get to the army is said storage folder
