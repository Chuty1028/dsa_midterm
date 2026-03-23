import random
import json

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

    def get_node_at(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                return current
            current = current.next
            i += 1
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


# Clase de song

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


# clase de playlist

class Playlist:
    def __init__(self, name):
        self.name = name
        self._list = DoublyLinkedList()
        self.current = None
        self._shuffle = False          
        self._shuffle_order = []       
        self._shuffle_index = 0       

    # operaciones basicas de la playlist

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

    # ── Playback controls ─────────────────────────────────────────────────────

    def play(self):
        if self.current:
            return self.current.data
        return None

    def next(self):
        if self._shuffle:
            if self._shuffle_index < len(self._shuffle_order) - 1:
                self._shuffle_index += 1
                idx = self._shuffle_order[self._shuffle_index]
                self.current = self._list.get_node_at(idx)
                return self.current.data
            return None  

        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None  

    def previous(self):
        if self._shuffle:
            if self._shuffle_index > 0:
                self._shuffle_index -= 1
                idx = self._shuffle_order[self._shuffle_index]
                self.current = self._list.get_node_at(idx)
                return self.current.data
            return None 

        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None  

    # Boton del shuffle

    def toggle_shuffle(self):
        self._shuffle = not self._shuffle

        if self._shuffle:
            
            indices = list(range(self._list.size))
            random.shuffle(indices)
            self._shuffle_order = indices
            self._shuffle_index = 0
            self.current = self._list.get_node_at(self._shuffle_order[0])
            print(f"[SHUFFLE ON]  Shuffle activated for '{self.name}'")
        else:
            self._shuffle_order = []
            self._shuffle_index = 0
            print(f"[SHUFFLE OFF] Shuffle deactivated for '{self.name}'")

    @property
    def shuffle_active(self):
        return self._shuffle

    # Display

    def show(self):
        shuffle_label = " [SHUFFLE ON]" if self._shuffle else ""
        print(f"\nPlaylist: {self.name}  ({len(self._list)} songs){shuffle_label}")
        print("-" * 55)
        current = self._list.head
        index = 1
        while current:
            marker = " << NOW PLAYING" if current is self.current else ""
            print(f"  {index:>3}. {current.data}{marker}")
            current = current.next
            index += 1
        print("-" * 55)

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self._list)} songs"

# INTERFAZ

def cargar_canciones_desde_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main():
    playlist = Playlist("Mi playlist")

    canciones = cargar_canciones_desde_json("songs_data.json")
    for c in canciones:
        playlist.add_song(Song(c["title"], c["artist"], c["album"]))

    while True:
        print("\n===== PLAYLIST =====")
        print("1. Play")
        print("2. Next")
        print("3. Previous")
        print("4. Mostrar playlist")
        print("5. Toggle Shuffle (ON/OFF)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            song = playlist.play()
            print(f"Reproduciendo: {song}")

        elif opcion == "2":
            song = playlist.next()
            print(f"Siguiente: {song}")

        elif opcion == "3":
            song = playlist.previous()
            print(f"Anterior: {song}")

        elif opcion == "4":
            playlist.show()

        elif opcion == "5":
            playlist.toggle_shuffle()
            estado = "ON" if playlist.shuffle_active else "OFF"
            print(f"Shuffle ahora está: {estado}")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
