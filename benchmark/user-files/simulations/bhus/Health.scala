package bhus

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class Health extends Simulation {

    val httpProtocol = http
      .baseUrl("http://localhost:8000")
      .acceptHeader("application/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
      .userAgentHeader("Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0")

    val scn = scenario("Health")
      .exec(http("request_1")
        .get("/healthz"))
      .pause(5)

    setUp(
      scn.inject(atOnceUsers(1))
    ).protocols(httpProtocol)
}
