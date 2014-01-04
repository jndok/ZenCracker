ZenCracker
==========

General informations
--------------------

Zen is a powerful hash brute-forcer, written in pure Python, released in late 2013. It is currently in BETA version, meaning it is not 100% completed. Here are some of the currently in-development Zen's features:

MD5, SHA-1, SHA-256, SHA-512 algorithms implementation
Two cracking methods, for now only one is available, the other is still under development
A 700MB big dictionary, containing 63941096 human passwords
An advanced hash-computing method, is a bit slow with large files, but works well also on old machines
Can work with basically every wordlist available online. (if set properly)
Fully customizable via a simple .config file.

In-depth informations and working mechanism
-------------------------------------------

Zen has two simple working mechanisms. Here they are:

**DHS - Dynamic Hash Scanning**

Zen loads up the dictionary file in chunks.
Zen starts to hash every single line of each chunk.
Zen loads all the hashes computed in a big table.
Zen tries to match the given hash with one in the table.
If there IS a match, the password is cracked. If there IS NOT a match, the password is not cracked.
Although this working routine may seem a bit sloppy and slow, is instead very effective, especially on old machines. The fact that Zen reads up chunks of data from the file, makes the work much faster. The user can customize the chunk size in the .config file, based on the power of his machine.

**PLHS - Pre-loaded Hash Scanning (STILL NOT IMPLEMENTED, USE DHS)**

Zen loads up the dictionary file in chunks.
Zen computes every hash in each chunk and saves them all in various external dictionaries (hashtabs).
Zen unloads the initial dictionary and loads the hashed dictionaries.
Zen tried to match the given hash with one in the hashed dictionaries.
If there IS a match, the password is cracked. If there IS NOT a match, the password is not cracked.
This method is not 100% completed and is not available for now. It's being designed to operate with VERY LARGE dictionaries, by firstly computing the hashes, and then saving the hashes in many little files, speeding up the cracking. This method also generates a lot of files, so if you have a slow computer, do not really use it for now. This method is useful to distribuite you hashtabs, so your friends can crack with them without computing the hashes. If your dictionary is below 3-4 GB, you can use the DHS method as well. It will be available in the next updates, when the code is less hacky and more stable.

How to use
----------

Zen is very easy to use. Once you start the program, you will see a shell-like prompt. You have to insert only two commands to start an attack.
Obviously, you'll need a dictionary (you can use the one included with Zen) in a readable format (like .txt or .dat). Then you'll need the hash you want to crack. Don't worry is you don't know which algorithm it uses, Zen will try to find out for you.
Now simply write open in the prompt and hit enter. You will now be asked for a dictionary. Drag&drop the file in the prompt,then hit enter.
Now that the list is loaded up, write hash in the prompt. You will be asked for the hash to crack, simply copy&paste the hash in the prompt and hit enter. If everything was done properly, Zen will inform you that the attack is ready to begin. Now press enter another time, and the attack will begin.

Now wait. If the file is very large, Zen will take a while to try all the hashes. Once Zen completes the crack, he will tell you if the password was found or not. If not, try with a better dictionary. The Internet is full of wordlists.

<ul>

  <li>[Very nice dictionary for WPA cracking (40GB extracted)]("http://maurisdump.blogspot.it/2011/12/best-dictionaries-wordlist-for-wpa.html")</li>
  <li>[Another big list of downloadable wordlists]("http://cyberwarzone.com/cyberwarfare/password-cracking-mega-collection-password-cracking-word-lists")</li>
  <li>[Big list of wordlist sites]("http://hashcat.net/forum/thread-1236.html")</li>
  <li>[Another list of wordlist sites (old though)]("http://www.room362.com/blog/2009/9/18/password-word-lists.html")</li>

</ul>

**Using the .config file**

Zen supports a .config file, where you can pre-load some settings, so you don't have to insert them every time you launch the program. Here are the supported settings for now:

<ul>

  <li>method | The method used for cracking (DHS or PLHS)</li>
  <li>dict | The path to the dictionary file.</li>
  <li>chunk_size | The size (in bytes) of the data that will be read when cracking.</li>

The .config file is found in the Zen folder, under the /config folder. I recommend not to use a chunk_size bigger than 1024. Bugs may occur if this size is exceeded. If the path to the dictionary file is not found, the user must input it manually via the open command.

</ul>
