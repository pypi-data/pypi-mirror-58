Ricecooker content upload process
=================================
This document describes the "behind the scenes" operation of the ricecooker library.




Build tree
----------
The ricececooker tree consists of `Node` and `File` objects organized into a tree
data structure.


Validation logic
----------------
Every ricecooker `Node` has a `validate` method that performs basic checks to
make sure the node's metadata is set correctly and necessary files are provided.

Each `File` subclass comes turn has it's own validation logic to ensure the file
provided has the appropriate extension.


File processing
---------------
The key moment during the upload process occurs when we call `process_files` on
each node object.

```python
filenames = node.process_files()
```


method is called 


process_file


File diff
---------

File upload
-----------






    # Authenticate user and check current Ricecooker version
    username, token = authenticate_user(token)
    check_version_number()
    channel = chef.get_channel(**kwargs)
    channel = chef.construct_channel(**kwargs)
    create_initial_tree(channel)
        tree.validate()
            channel.validate_tree()

Extract

    process_tree_files(tree)
        files_to_diff = tree.process_tree(tree.channel)
            file_names = []
            self.process_tree_recur(file_names, channel_node)
            return [x for x in set(file_names) if x]  # Remove any duplicate or None filenames
        tree.check_for_files_failed()
            config.LOGGER.warning ... files failed to download
        return files_to_diff, config.FAILED_FILES

    get_file_diff(tree, files_to_diff)
        tree.get_file_diff(files_to_diff)
            config.SESSION.post(config.file_diff_url()

Load:

    upload_files(tree, file_diff)
        tree.upload_files(file_diff)
        tree.reattempt_upload_fails()
    create_tree(tree)
        channel_id, channel_link = tree.upload_tree()
    publish_tree(tree, channel_id)
        tree.publish(channel_id)

