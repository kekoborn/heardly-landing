import CoreGraphics
import Foundation
// Ждём, пока поповер (слой 25) окажется на экране, и печатаем его id.
let deadline = Date().addingTimeInterval(8)
while Date() < deadline {
    let info = CGWindowListCopyWindowInfo([.optionOnScreenOnly], kCGNullWindowID) as? [[String: Any]] ?? []
    for w in info where (w[kCGWindowOwnerName as String] as? String ?? "").contains("Heardly") {
        if (w[kCGWindowLayer as String] as? Int ?? 0) == 25 {
            print(w[kCGWindowNumber as String] as? Int ?? 0)
            exit(0)
        }
    }
    usleep(60_000)
}
exit(1)
