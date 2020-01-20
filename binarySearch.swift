import Foundation

extension Array where Element: Comparable {
	func binarySearch(_ toFind: Element) -> Bool {
		self[0...].binarySearch(toFind)
	}
}

extension ArraySlice where Element: Comparable {
	func binarySearch(_ toFind: Element) -> Bool {
		guard count > 0 else { return false }

		let middle = count / 2

		if self[middle] == toFind {
			return true
		} else if toFind < self[middle] {
			return self[..<middle].binarySearch(toFind)
		} else {
			return self[(middle + 1)...].binarySearch(toFind)
		}
	}
}

let alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(separator: " ")
print(alpha)

print(alpha.binarySearch("a"))
print(alpha.binarySearch("A"))