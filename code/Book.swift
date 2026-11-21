import Foundation

final class Book {
    private let id: Int
    private let title: String
    private let author: String

    init(id: Int, title: String, author: String) {
        self.id = id
        self.title = title
        self.author = author
    }
}
