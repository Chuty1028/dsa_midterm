class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_after(self, target_data, data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.size += 1
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def traverse_forward(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def traverse_backward(self):
        elements = []
        current = self.tail
        while current:
            elements.append(current.data)
            current = current.prev
        return elements

    def __len__(self):
        return self.size

    def __str__(self):
        elements = self.traverse_forward()
        return " <-> ".join(str(e) for e in elements) if elements else "Empty list"


class Song:
    def __init__(self, title, artist, album, duration=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self):
        return f"{self.title} - {self.artist} [{self.album}]"

    def __eq__(self, other):
        if isinstance(other, Song):
            return self.title == other.title and self.artist == other.artist
        return False


class Playlist:
    def __init__(self, name):
        self.name = name
        self._list = DoublyLinkedList()
        self.current = None

    def add_song(self, song):
        self._list.append(song)
        if self.current is None:
            self.current = self._list.head

    def add_song_at_beginning(self, song):
        self._list.prepend(song)
        self.current = self._list.head

    def add_song_after(self, target_song, song):
        return self._list.insert_after(target_song, song)

    def remove_song(self, song):
        if self.current and self.current.data == song:
            self.current = self.current.next or self.current.prev
        return self._list.delete(song)

    def search_song(self, title):
        current = self._list.head
        while current:
            if current.data.title.lower() == title.lower():
                return current.data
            current = current.next
        return None

    def play_current(self):
        return self.current.data if self.current else None

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def show(self):
        print(f"\nPlaylist: {self.name}  ({len(self._list)} songs)")
        print("-" * 50)
        current = self._list.head
        index = 1
        while current:
            marker = " << NOW PLAYING" if current is self.current else ""
            print(f"  {index:>3}. {current.data}{marker}")
            current = current.next
            index += 1
        print("-" * 50)

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self._list)} songs"